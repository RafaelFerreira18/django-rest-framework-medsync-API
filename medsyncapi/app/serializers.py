from rest_framework import serializers
from .models import Patient, Doctor, Appointment, Specialties

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class SpecialtiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialties
        fields = '__all__'
