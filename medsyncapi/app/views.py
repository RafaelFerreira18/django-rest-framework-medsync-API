import os
import environ
from rest_framework import viewsets

from medsyncapi.settings import BASE_DIR
from .models import Patient, Doctor, Appointment, Specialty
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, SpecialtiesSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework.response import Response
import smtplib

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

    @action(detail=True, methods=['post'])
    def schedule(self, request):
        print("Scheduling appointment...")
        appointment = self.get_object()
        doctor = appointment.doctor
        env = environ.Env()
        s = smtplib.SMTP(env('SMTP_HOST'), env('SMTP_PORT'))
        s.starttls()
        s.login(env("SMTP_LOGIN_GMAIL"), env("SMTP_PASSWORD_GMAIL"))
        msg = f"Subject: Appointment Confirmation\n\nYour appointment has been scheduled with {doctor.name}."
        s.sendmail(env("SMTP_LOGIN_GMAIL"), request.data.get('email'), msg)
        s.quit()
        appointment.date = request.data.get('date')
        appointment.save()
        return Response({'status': 'appointment scheduled', 'appointment': AppointmentSerializer(appointment).data})

class SpecialtiesViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtiesSerializer
