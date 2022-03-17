from django.urls import path
from . import views


urlpatterns = [
    path('vacancies/', views.VacancyAPIView.as_view()),
    path('directions/', views.GetDirectionsAPIView.as_view()),
    path('work_times/', views.GetWorkTimeAPIView.as_view()),
    path('degree/', views.GetDegreeAPIView.as_view()),
    path('experience/', views.GetExperienceAPIView.as_view()),
    path('english_level/', views.GetEnglishLevelAPIView.as_view()),
    path('resumes/', views.ResumeAPIView.as_view()),
    path('amount/', views.AmountVacancyResumeAPIView.as_view()),
]
