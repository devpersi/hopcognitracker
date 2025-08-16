from django.contrib import admin
from django.forms.widgets import Textarea
from .services.attempt_services import create_attempt_with_answers
# Register your models here.
from .models import Doctor, Patient, Questionnaire, Attempt, Question, Answer, QuestionCodeDescription
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Questionnaire)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'question_text':
            kwargs['widget'] = Textarea
        return super().formfield_for_dbfield(db_field, request, **kwargs)

admin.site.register(QuestionCodeDescription)

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('patient', 'administered_by_doctor', 'questionnaire', 'status', 'scheduled_for', 'created_at', 'updated_at')
    list_filter = ('status', 'administered_by_doctor')
    search_fields = ('patient__first_name', 'patient__last_name', 'questionnaire__title')
    inlines = [AnswerInline]
    
    def save_related(self, request, form, formsets, change) -> None:
        super().save_related(request, form, formsets, change)
        if not change and form.instance:
            create_attempt_with_answers(form.instance)