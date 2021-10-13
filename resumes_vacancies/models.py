import datetime

from django.db import models


# Create your models here.

class DirectionsModel(models.Model):
    """
    Direction model for Vacancies and Resumes
    """
    direction = models.CharField(verbose_name='Напрям роботи', max_length=90)

    def __str__(self):
        return self.direction


class WorkTimeModel(models.Model):
    """
    Work Time model for Students Resumes
    """
    work_time = models.CharField(verbose_name='Бажаний вид діяльності', max_length=90)


class VacancyModel(models.Model):
    """
    Vacancy model
    """
    company_name = models.CharField(verbose_name='Назва компанії', max_length=45)
    company_short_description = models.TextField(verbose_name='Короткий опис компанії (якщо ви з нами вже знайомі, '
                                                              'то можете лишити поле пустим)', blank=True)
    company_direction = models.ForeignKey(to='DirectionsModel', on_delete=models.RESTRICT)
    vacancy_name = models.CharField(verbose_name='Назва вакансії', max_length=45)
    vacancy_description = models.TextField(verbose_name='Опис вакансії та обов\'язки')
    vacancy_requirements = models.TextField(verbose_name='Вимоги до кандидата')
    vacancy_working_conditions = models.TextField(verbose_name='Умови праці')
    vacancy_salary = models.CharField(verbose_name='Грошова винагорода', max_length=20)
    vacancy_benefits = models.TextField(verbose_name='Переваги')
    vacancy_contacts = models.TextField(verbose_name='Контакти')
    company_website = models.TextField(verbose_name='Посилання на сайт компанії', blank=True)
    vacancy_date_added = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_for_yesterday():
        return VacancyModel.objects.filter(vacancy_date_added__range=(datetime.datetime.now(), datetime.datetime.now()
                                                                      - datetime.timedelta(1))).values_list()

    class Meta:
        ordering = ['vacancy_date_added']


class ResumeModel(models.Model):
    """
    Resume model
    """

    def upload_to_user(self, filename):
        return f'resumes/{self.students_pib.replace(" ", "_")}/{filename}'

    students_pib = models.CharField(verbose_name='П.І.Б.', max_length=90)
    students_phone_number = models.CharField(verbose_name='Номер телефону', max_length=50)
    students_email = models.CharField(verbose_name='Електронна пошта', max_length=90)
    students_direction = models.ForeignKey(to='DirectionsModel', on_delete=models.RESTRICT)
    students_work_time = models.ManyToManyField(to='WorkTimeModel', related_name='work_time_list')
    students_resume_file = models.FileField(verbose_name='Резюме (PDF)', upload_to=upload_to_user, blank=True,
                                            null=True)
    students_resume_link = models.TextField(verbose_name='Посилання на портфолія', blank=True, null=True)
    resume_date_added = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_for_yesterday():
        return ResumeModel.objects.filter(resume_date_added__range=(datetime.datetime.now(), datetime.datetime.now()
                                                                    - datetime.timedelta(1))).values_list()
