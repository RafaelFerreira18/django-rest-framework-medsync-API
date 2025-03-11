from rest_framework import viewsets
from .models import Patient, Doctor, Appointment, Specialties
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, SpecialtiesSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class SpecialtiesViewSet(viewsets.ModelViewSet):
    queryset = Specialties.objects.all()
    serializer_class = SpecialtiesSerializer
