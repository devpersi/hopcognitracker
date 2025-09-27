from rest_framework import viewsets
from medical.models import Doctor, Patient, Attempt
from medical.api.serializers import DoctorSerializer, PatientSerializer, AttemptSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('-created_at')
    serializer_class = DoctorSerializer
    
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('-created_at')
    serializer_class = PatientSerializer
    
class AttemptViewSet(viewsets.ModelViewSet):
    queryset = Attempt.objects.all().order_by('-created_at')
    serializer_class = AttemptSerializer