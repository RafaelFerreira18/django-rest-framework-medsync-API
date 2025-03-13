from rest_framework import viewsets
from .models import Patient, Doctor, Appointment, Specialty
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, SpecialtiesSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class SpecialtiesViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtiesSerializer
