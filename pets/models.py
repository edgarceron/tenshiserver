from django.db import models
from authentication.models import CustomUser
# Create your models here.
class Pets(models.Model):
    """Model to represent a pet"""
    name = models.TextField()
    race = models.TextField(null=True)
    picture = models.FileField(null=True)
    size = models.TextField(null=True)
    age = models.IntegerField(null=True)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)

class Veterinary(models.Model):
    """Model to represent a veterinarie, the organization that will attend appoinmetns"""
    name = models.TextField()
    address = models.TextField()
    phone = models.TextField()
    email = models.TextField()
    social_networks = models.TextField()
    plan = models.TextField()
    photo = models.FieldFile(null=True)
    active = models.BooleanField()

class Profesional(models.Model):
    """Model to represent a profesional, e.g Nurse, Veterinary, Laboratorian"""
    name = models.TextField()
    type = models.TextField()
    active = models.BooleanField()

class ClinicHistory(models.Model):
    """Model to represent a pet's Clinic history"""
    pet = models.ForeignKey(Pets, null=False, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, null=False)
    date = models.DateTimeField(null=False)
    incident_type = models.TextField(null=False)
    file = models.FieldFile(null=True)
    comments = models.TextField(null=True)

class TestResults(models.Model):
    """Model to represent the test results of a test took on a pet"""
    pet = models.ForeignKey(Pets, null=False, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, null=False)
    date = models.DateTimeField(null=False)
    result = models.TextField(null=False)
    comments = models.TextField(null=True)

class ProgrammedAppointment(models.Model):
    """Model to represent programmed appointments for pets"""
    pet = models.ForeignKey(Pets, null=False, on_delete=models.CASCADE)
    veterinary = models.ForeignKey(Veterinary, null=False)
    frequency = models.IntegerField(null=True)
    active = models.BooleanField()

class Appointment(models.Model):
    """Model to represent appointments for pets"""
    pet = models.ForeignKey(Pets, null=False, on_delete=models.CASCADE)
    programmed_appointment = models.ForeignKey(ProgrammedAppointment, null=True)
    profesional = models.ForeignKey(Profesional, null=False)
    clinic_history = models.ForeignKey(ClinicHistory, null=False)
    date = models.DateTimeField(null=False)
    comments = models.TextField(null=True)

class Reviews(models.Model):
    """Model to represent reviews from users to veterinaries"""
    veterinary = models.ForeignKey(Veterinary, null=False)
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.CASCADE)
    rate = models.IntegerField()
    comments = models.TextField(null=False)
