from django.contrib import admin
from . import models


# Register your models here.


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_direction', 'vacancy_name', 'vacancy_salary', 'vacancy_date_added')

    
admin.site.register(models.DirectionsModel)
admin.site.register(models.VacancyModel, VacancyAdmin)
admin.site.register(models.ResumeModel)
admin.site.register(models.WorkTimeModel)
admin.site.register(models.DegreeModel)
admin.site.register(models.ExperienceModel)
admin.site.register(models.EnglishLevelModel)
