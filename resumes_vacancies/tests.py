from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from resumes_vacancies import models


class SecondaryModelsTests(APITestCase):
    def setUp(self):
        self.direction = models.DirectionsModel.objects.create(direction='Розваги')
        self.work_time = models.WorkTimeModel.objects.create(work_time=r'24\7 без вихідних')
        self.degree = models.DegreeModel.objects.create(degree='Без освіти')
        self.experience = models.ExperienceModel.objects.create(experience='Професіонал з багаторічним досвідом')
        self.english_level = models.EnglishLevelModel.objects.create(level='Мінімальний')

        self.urls = ('directions', 'work_time', 'degrees', 'experiences', 'english_levels', 'directions')

    def test_get_list(self):
        for url in self.urls:
            with self.subTest():
                response = self.client.get(reverse(url))
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), 1)


class VacancyTests(APITestCase):
    def setUp(self):
        self.direction = models.DirectionsModel.objects.create(direction='IT')
        self.vacancy = models.VacancyModel.objects.create(
            company_name='Google', company_short_description='Corporation of Evil', company_direction=self.direction,
            vacancy_name='Cleaner', vacancy_description='Just a Cleaner', vacancy_requirements='Be a Slave',
            vacancy_working_conditions='Working outside', vacancy_salary='No Salary', vacancy_benefits='No benefits',
            vacancy_contacts='https://google.com', company_website='https://google.com'
        )

    def test_vacancy_list(self):
        response = self.client.get(reverse('vacancies'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_vacancy(self):
        work_time = models.WorkTimeModel.objects.create(work_time='On Weekends')
        degree = models.DegreeModel.objects.create(degree='No Degree')
        experience = models.ExperienceModel.objects.create(experience='Need a Professional')

        data = {
            'company_name': 'Google', 'company_short_description': 'Corporation of Evil',
            'vacancy_name': 'Cleaner', 'company_direction': self.direction.id, 'vacancy_description': 'Just a Cleaner',
            'working_time': [work_time.id], 'vacancy_requirements': 'Be a Slave',
            'vacancy_working_conditions': 'Working outside', 'vacancy_degree': [degree.id],
            'working_experience': [experience.id], 'vacancy_salary': 'No Salary', 'vacancy_benefits': 'No benefits',
            'vacancy_contacts': 'https://google.com', 'company_website': 'https://google.com'
        }

        response = self.client.post(reverse('vacancies'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(reverse('vacancies'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class ResumeTests(APITestCase):
    def setUp(self):
        self.direction = models.DirectionsModel.objects.create(direction='Література')
        self.resume = models.ResumeModel.objects.create(
            students_pib='Шевченко Тарас Григорович', students_phone_number='+380101010101',
            students_email='Taras@gmail.com', students_direction=self.direction
        )

    def test_resume_list(self):
        response = self.client.get(reverse('resumes'))
        self.assert_(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_resume(self):
        work_time = models.WorkTimeModel.objects.create(work_time='On Weekends')
        data = {
            'students_pib': 'Франок Іван Якович', 'students_phone_number': '+380777777777',
            'students_email': 'Ivan@gmail.com', 'students_direction': self.direction.id,
            'students_work_time': [work_time.id]
        }

        response = self.client.post(reverse('resumes'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(reverse('resumes'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class GetAmountTests(APITestCase):
    def test_get_amount(self):
        direction = models.DirectionsModel.objects.create(direction='IT')
        response = self.client.get(reverse('amount'))
        self.assertEqual(response.data['vacancy_amount'], 0)
        self.assertEqual(response.data['resume_amount'], 0)

        self.resume = models.ResumeModel.objects.create(
            students_pib='Шевченко Тарас Григорович', students_phone_number='+380101010101',
            students_email='Taras@gmail.com', students_direction=direction
        )
        self.vacancy = models.VacancyModel.objects.create(
            company_name='Google', company_short_description='Corporation of Evil', company_direction=direction,
            vacancy_name='Cleaner', vacancy_description='Just a Cleaner', vacancy_requirements='Be a Slave',
            vacancy_working_conditions='Working outside', vacancy_salary='No Salary', vacancy_benefits='No benefits',
            vacancy_contacts='https://google.com', company_website='https://google.com'
        )

        response = self.client.get(reverse('amount'))
        self.assertEqual(response.data['vacancy_amount'], 1)
        self.assertEqual(response.data['resume_amount'], 1)
