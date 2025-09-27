from django.urls import path, include
from . import views
from . import views_create_edit

urlpatterns = [
    # index page for medical app
    # ex: /medical/
    path('', views.IndexView.as_view(), name='medical_index'),
    
    # doctor-related URLs
    # ex: /medical/doctors/
    path('doctors/', views.DoctorListView.as_view(), name='doctor_list'),
    # ex: /medical/doctor/5/
    path('doctor/<int:doctor_id>/', views.DoctorDetailView.as_view(), name='doctor_detail'),
    # ex: /medical/doctors/create/
    path('doctors/create', views_create_edit.DoctorCreateView.as_view(), name='doctor_create'),
    # ex: /medical/doctors/edit/5/
    path('doctors/edit/<int:doctor_id>/', views_create_edit.DoctorUpdateView.as_view(), name='doctor_edit'),
    
    # patient-related URLs
    # ex: /medical/patients/
    path('patients/', views.PatientListView.as_view(), name='patient_list'),
    # ex: /medical/patient/5/
    path('patient/<int:patient_id>/', views.PatientDetailView.as_view(), name='patient_detail'),
    # ex: /medical/patients/create/
    path('patients/create', views_create_edit.PatientCreateView.as_view(), name='patient_create'),
    # ex: /medical/patients/edit/5/
    path('patients/edit/<int:patient_id>/', views_create_edit.PatientUpdateView.as_view(), name='patient_edit'),
    
    
    # questionnaire-related URLs
    # ex: /medical/questionnaires/
    path('questionnaires/', views.QuestionnaireListView.as_view(), name='questionnaire_list'),
    # ex: /medical/questionnaire/5/
    path('questionnaire/<int:questionnaire_id>/', views.QuestionnaireDetailView.as_view(), name='questionnaire_detail'),
    
    # attempt-related URLs
    # ex: /medical/attempts/
    path('attempts/', views.AttemptListView.as_view(), name='attempt_list'),
    # ex: /medical/attempt/5/
    path('attempt/<int:attempt_id>/', views.AttemptDetailView.as_view(), name='attempt_detail'),
    # ex: /medical/attempts/create/
    path('attempts/create', views_create_edit.AttemptCreateView.as_view(), name='attempt_create'),
    # ex: /medical/attempts/edit/5/
    path('attempts/edit/<int:attempt_id>/', views_create_edit.AttemptUpdateView.as_view(), name='attempt_edit'),
    
    # api urls
    # ex: /medical/api
    path('api/', include('medical.api.urls')),
]
