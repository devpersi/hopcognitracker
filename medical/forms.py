from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Doctor, Patient, Attempt, Answer

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
        }
    
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'caretaker_first_name', 
                  'caretaker_last_name', 'caretaker_phone_number', 
                  'caretaker_relationship', 'caretaker_email', 'overseen_by_doctor']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'caretaker_first_name': forms.TextInput(attrs={'placeholder': 'Caretaker First Name'}),
            'caretaker_last_name': forms.TextInput(attrs={'placeholder': 'Caretaker Last Name'}),
            'caretaker_phone_number': forms.TextInput(attrs={'placeholder': 'Caretaker Phone Number'}),
            'caretaker_relationship': forms.TextInput(attrs={'placeholder': 'Relationship to Patient'}),
            'caretaker_email': forms.EmailInput(attrs={'placeholder': 'Caretaker Email'}),
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer', 'is_needed', 'is_covered', 'notes']
        widgets = {
            'answer': forms.CheckboxInput(),
            'is_needed': forms.CheckboxInput(),
            'is_covered': forms.CheckboxInput(),
            'notes': forms.Textarea(attrs={'placeholder': 'Additional Notes'}),
        }
        
class AttemptForm(ModelForm):
    class Meta:
        model = Attempt
        fields = ['patient', 'administered_by_doctor', 'questionnaire', 
                  'status', 'scheduled_for', ]
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'administered_by_doctor': forms.Select(attrs={'class': 'form-control'}),
            'questionnaire': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'scheduled_for': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
AnswerFormSet = inlineformset_factory(Attempt, Answer, form=AnswerForm, extra=0, can_delete=False)