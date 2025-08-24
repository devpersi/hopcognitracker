from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Doctor {self.first_name[:1]}. {self.last_name}"

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    caretaker_first_name = models.CharField(max_length=100, blank=True, null=True)
    caretaker_last_name = models.CharField(max_length=100, blank=True, null=True)
    caretaker_phone_number = models.CharField(max_length=15, blank=True, null=True)
    caretaker_relationship = models.CharField(max_length=50, blank=True, null=True)
    caretaker_email = models.EmailField(null=True, blank=True)
    overseen_by_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patients')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Patient {self.first_name[:1]}. {self.last_name}"

class Questionnaire(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return f"Questionnaire {self.title[:10]} + ..."
    
class Attempt(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='attempts')
    administered_by_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='attempts')
    status = models.CharField(max_length=20, choices=[
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ])
    scheduled_for = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"Attempt for {self.patient.first_name[:1]}. {self.patient.last_name} on {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    
class Question(models.Model):
    question_code = models.CharField(max_length=50, unique=True)
    question_text = models.CharField(max_length=500)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return f"{self.question_code} Question: {self.question_text[:10]}..."
    
class QuestionCodeDescription(models.Model):
    question_code_prefix = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.question_code_prefix} Description: {self.description[:10]}..."
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE, related_name='answers')
    answer = models.BooleanField(default=False)
    is_needed = models.BooleanField(default=False)
    is_covered = models.BooleanField(default=False)
    notes = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'attempt'], name='unique_question_attempt')
        ]

    def __str__(self):
        return f"{self.question.question_code} Answer to {self.question.question_text[:10]}... for {self.attempt.patient.last_name}"