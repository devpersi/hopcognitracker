from rest_framework import serializers
from medical.models import Doctor, Patient, Answer, Attempt
from medical.services.attempt_services import create_attempt_with_answers

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question','answer', 'is_needed', 'is_covered', 'notes')
        
class AttemptSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=False, required=False)
    
    class Meta:
        model = Attempt
        fields = ('id', 'patient', 'questionnaire', 'status', 'scheduled_for', 'administered_by_doctor', 'answers')
        
    def create(self, validated_data):
        attempt = Attempt.objects.create(**validated_data)
        create_attempt_with_answers(attempt)
        return attempt
    
    def update(self, instance, validated_data):
        instance.patient = validated_data.get('patient', instance.patient)
        instance.questionnaire = validated_data.get('questionnaire', instance.questionnaire)
        instance.status = validated_data.get('status', instance.status)
        instance.scheduled_for = validated_data.get('scheduled_for', instance.scheduled_for)
        instance.administered_by_doctor = validated_data.get('administered_by_doctor', instance.administered_by_doctor)
        
        answers_data = validated_data.get('answers', [])
        for answer_data in answers_data:
            answer = instance.answers.get(question=answer_data['question'])
            answer.answer = answer_data['answer']
            answer.is_needed = answer_data['is_needed']
            answer.is_covered = answer_data['is_covered']
            answer.notes = answer_data['notes']
            answer.save()
            
        instance.save()
        return instance