from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default=None, null=True, blank=True)
    birth_date = models.DateField(default=None, null=True, blank=True)

    class Meta:
        abstract = True

class Patient(Person):
    age = models.IntegerField()
    cpf = models.CharField(max_length=11)

class Specialty(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Doctor(Person):
    crm = models.CharField(max_length=7)
    specialties = models.ManyToManyField(Specialty, related_name="doctors")
    def __str__(self):
        return self.name

class Appointment(models.Model):
    date = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f'{self.patient.name} - {self.doctor.name}'

    
