from django.urls import path
from . import views

urlpatterns = [
    # ex: /medical/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /medical/doctors/
    path('doctors/', views.DoctorListView.as_view(), name='doctor_list'),
    # ex: /medical/doctor/5/
    path('doctor/<int:doctor_id>/', views.DoctorDetailView.as_view(), name='doctor_detail'),
    # ex : /medical/patients/
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
    # ex: /medical/patient/5/
    path('patient/<int:patient_id>/', views.PatientDetailView.as_view(), name='patient_detail'),
    # ex: /medical/questionnaires/
    path('questionnaires/', views.QuestionnaireListView.as_view(), name='questionnaire_list'),
    # ex: /medical/questionnaire/5/
    path('questionnaire/<int:questionnaire_id>/', views.QuestionnaireDetailView.as_view(), name='questionnaire_detail'),
    # ex: /medical/attempts/
    path('attempts/', views.AttemptListView.as_view(), name='attempt_list'),
    # ex: /medical/attempt/5/
    path('attempt/<int:attempt_id>/', views.AttemptDetailView.as_view(), name='attempt_detail'),
]
