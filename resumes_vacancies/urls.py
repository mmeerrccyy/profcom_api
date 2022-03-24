from django.urls import path
from . import views


urlpatterns = [
    path('directions/', views.GetDirectionsAPIView.as_view(), name='directions'),
    path('work_time/', views.GetWorkTimeAPIView.as_view(), name='work_time'),
    path('degrees/', views.GetDegreeAPIView.as_view(), name='degrees'),
    path('experiences/', views.GetExperienceAPIView.as_view(), name='experiences'),
    path('english_levels/', views.GetEnglishLevelAPIView.as_view(), name='english_levels'),

    path('vacancies/', views.VacancyAPIView.as_view(), name='vacancies'),
    path('resumes/', views.ResumeAPIView.as_view(), name='resumes'),

    path('amount/', views.AmountVacancyResumeAPIView.as_view(), name='amount'),
]
