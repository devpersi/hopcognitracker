from django.views.generic import CreateView, UpdateView
from .models import Doctor, Patient, Attempt
from .forms import DoctorForm, PatientForm, AttemptForm, AnswerFormSet
from django.urls import reverse
from .services.attempt_services import create_attempt_with_answers

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'medical/form/doctor.html'
    success_url = '/medical/doctors/'
    
class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'medical/form/doctor.html'
    success_url = '/medical/doctors/'
    pk_url_kwarg = 'doctor_id'
    
class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'medical/form/patient.html'
    success_url = '/medical/patients/'
    
class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'medical/form/patient.html'
    success_url = '/medical/patients/'
    pk_url_kwarg = 'patient_id'
    
class AttemptCreateView(CreateView):
    model = Attempt
    form_class = AttemptForm
    template_name = 'medical/form/attempt.html'
    
    def form_valid(self, form):
        self.object = form.save()
        create_attempt_with_answers(self.object)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('attempt_edit', kwargs={'attempt_id': self.object.id})
    
class AttemptUpdateView(UpdateView):
    model = Attempt
    form_class = AttemptForm
    template_name = 'medical/form/attempt.html'
    success_url = '/medical/attempts/'
    pk_url_kwarg = 'attempt_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        attempt = self.object
        
        if self.request.POST:
            context['answer_formset'] = AnswerFormSet(self.request.POST, instance=attempt)
        else:
            context['answer_formset'] = AnswerFormSet(instance=attempt)
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        answer_formset = context['answer_formset']
        
        if form.is_valid() and answer_formset.is_valid():
            self.object = form.save()
            answer_formset.instance = self.object
            answer_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)