from .models import Doctor, Patient, Questionnaire, Attempt, QuestionCodeDescription, Answer
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'medical/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctor_list'] = Doctor.objects.order_by('-created_at')[:10]  # Get the last 10 doctors
        context['patient_list'] = Patient.objects.order_by('-created_at')[:10]  # Get the last 10 patients
        context['questionnaire_list'] = Questionnaire.objects.all()[:10]  # Get the last 10 questionnaires
        context['attempt_list'] = Attempt.objects.order_by('-created_at')[:10]  # Get the last 10 attempts
        context['year'] = 2025
        return context

class DoctorListView(ListView):
    model = Doctor
    template_name = 'medical/doctors.html'
    context_object_name = 'doctor_list'
    ordering = ['last_name']

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'medical/doctor.html'
    context_object_name = 'doctor'
    pk_url_kwarg = 'doctor_id'
    
class PatientListView(ListView):
    model = Patient
    template_name = 'medical/patients.html'
    context_object_name = 'patient_list'
    ordering = ['last_name']

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'medical/patient.html'
    context_object_name = 'patient'
    pk_url_kwarg = 'patient_id'
    
class QuestionnaireListView(ListView):
    model = Questionnaire
    template_name = 'medical/questionnaires.html'
    context_object_name = 'questionnaire_list'
    ordering = ['title']

class QuestionnaireDetailView(DetailView):
    model = Questionnaire
    template_name = 'medical/questionnaire.html'
    context_object_name = 'questionnaire'
    pk_url_kwarg = 'questionnaire_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_codes'] = QuestionCodeDescription.objects.all()
        return context

class AttemptListView(ListView):
    model = Attempt
    template_name = 'medical/attempts.html'
    context_object_name = 'attempt_list'
    ordering = ['-created_at']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_list'] = Patient.objects.all()
        return context

class AttemptDetailView(DetailView):
    model = Attempt
    template_name = 'medical/attempt.html'
    context_object_name = 'attempt'
    pk_url_kwarg = 'attempt_id'