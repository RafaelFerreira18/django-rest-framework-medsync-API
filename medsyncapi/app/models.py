from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Patient(Person):
    age = models.IntegerField()
    cpf = models.CharField(max_length=11)

class Doctor(Person):
    crm = models.CharField(max_length=7)

class Appointment(models.Model):
    date = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.patient.name} - {self.doctor.name}'

class Specialties(models.Model):
    name = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
