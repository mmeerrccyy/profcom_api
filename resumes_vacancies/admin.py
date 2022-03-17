from django.contrib import admin
from . import models


# Register your models here.


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_direction', 'vacancy_name', 'vacancy_salary', 'vacancy_date_added')


admin.site.register(models.VacancyModel, VacancyAdmin)

tuple_models = (models.DirectionsModel, models.ResumeModel, models.WorkTimeModel, models.DegreeModel,
                models.ExperienceModel, models.EnglishLevelModel)

for model in tuple_models:
    admin.site.register(model)
