from django.core.management import BaseCommand
from django.conf import settings
from resumes_vacancies import models

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

import os


class Command(BaseCommand):
    """
    Command for parsing vacancies from Google Sheet
    """
    base_dir = settings.BASE_DIR
    access_to_sheet_dir = os.path.join(base_dir, 'resumes_vacancies', 'management', 'commands', 'access_to_sheet')
    credentials_dir = str(os.path.join(access_to_sheet_dir, 'credentials.json'))
    token_dir = str(os.path.join(access_to_sheet_dir, 'token.json'))

    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    titles = (
        'company_name', 'company_short_description', 'company_direction', 'vacancy_name',
        'vacancy_description', 'vacancy_requirements', 'vacancy_working_conditions',
        'vacancy_salary', 'vacancy_benefits', 'vacancy_contacts', 'company_website',
        'vacancy_degree', 'minimal_english_level', 'working_time', 'working_experience'
    )

    spreadsheet_id = '1nU3wT-ywI5ePxhRVEksmxQDem-TJfCbsoZBsBerdnOM'
    sheet_range = 'B2:P'
    sheet_title = 'Form Responses 1'

    def connect_to_sheet_api(self):
        """"
        Creating connection to Google Sheet API, getting scopes,
        spreadsheet's id and range. Checking if credentials and tokens are valid
        """
        credentials = None

        if os.path.exists(self.token_dir):
            credentials = Credentials.from_authorized_user_file(self.token_dir, self.scopes)

        # If there are no (valid) credentials available, let the user log in.
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_dir, self.scopes)
                credentials = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open(self.token_dir, 'w') as token:
                token.write(credentials.to_json())

        # Connect to spreadsheet
        service = build('sheets', 'v4', credentials=credentials)
        sheet = service.spreadsheets()

        return sheet

    def get_vacancies_from_sheet(self, spreadsheet):
        """
        Collecting Vacancies data from spreadsheet
        """
        values_response = spreadsheet.values().get(spreadsheetId=self.spreadsheet_id,
                                                   range=f"{self.sheet_title}!{self.sheet_range}").execute()
        values = values_response.get('values', [])

        assert values, f'No values in {self.sheet_title}'

        # Create dict with vacancy details
        for value in values:
            vacancy_details = {title: '' for title in self.titles}
            vacancy_details.update({self.titles[i]: value[i].strip() for i in range(len(value))})

            for title in ('working_time', 'vacancy_degree', 'working_experience'):
                vacancy_details[title] = vacancy_details[title].split(', ')
                if vacancy_details[title] == ['']:
                    vacancy_details[title] = []

            yield vacancy_details

    @staticmethod
    def get_entities(vacancy_details, title, model, model_property):
        """
        Getting list of models that have relationships with Vacancies
        """
        entities = []
        entities_names = vacancy_details[title]

        if type(entities_names) is list:
            for entity_name in vacancy_details[title]:
                kwarg = {model_property: entity_name}
                entity = model.objects.filter(**kwarg).first()

                if entity:
                    entities.append(entity)

        elif type(entities_names) is str:
            kwarg = {model_property: entities_names}
            entity = model.objects.filter(**kwarg).first()

            if entity:
                entities.append(entity)

        else:
            raise Exception(f"{vacancy_details[title]} value can be list or str")

        return entities

    def handle(self, *args, **options):
        print('Start checking Google Sheet')
        sheet = self.connect_to_sheet_api()

        for vacancy in self.get_vacancies_from_sheet(sheet):
            company_direction = self.get_entities(vacancy, 'company_direction', models.DirectionsModel, 'direction')
            working_time = self.get_entities(vacancy, 'working_time', models.WorkTimeModel, 'work_time')
            vacancy_degree = self.get_entities(vacancy, 'vacancy_degree', models.DegreeModel, 'degree')
            working_experience = self.get_entities(vacancy, 'working_experience', models.ExperienceModel, 'experience')
            minimal_english_level = self.get_entities(vacancy, 'minimal_english_level', models.EnglishLevelModel,
                                                      'level')
            del vacancy['working_time']
            del vacancy['vacancy_degree']
            del vacancy['working_experience']

            vacancy['company_direction'] = company_direction[0]

            if minimal_english_level:
                vacancy['minimal_english_level'] = minimal_english_level[0]
            else:
                del vacancy['minimal_english_level']

            if not models.VacancyModel.objects.filter(**vacancy).exists():
                created_vacancy = models.VacancyModel.objects.create(**vacancy)
                created_vacancy.working_time.set(working_time)
                created_vacancy.vacancy_degree.set(vacancy_degree)
                created_vacancy.working_experience.set(working_experience)
                print(f'Vacancy added {created_vacancy.vacancy_name}')

        print('Script is finished')
