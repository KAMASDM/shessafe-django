from django.conf import settings
from django.db import models

class SafetyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    health_word_audio = models.FileField(upload_to='health_audio/', null=True, blank=True)
    health_word_text = models.CharField(max_length=100)
    health_contact1 = models.CharField(max_length=15,blank=True, null=True)
    health_contact2 = models.CharField(max_length=15,blank=True, null=True)
    health_contact3 = models.CharField(max_length=15,blank=True, null=True)
    ambulance_contact = models.CharField(max_length=15,blank=True, null=True)
    family_doctor_contact = models.CharField(max_length=15,blank=True, null=True)
    nearest_hospital_location = models.CharField(max_length=255,blank=True, null=True)

    threat_word_audio = models.FileField(upload_to='threat_audio/', null=True, blank=True)
    threat_word_text = models.CharField(max_length=100)
    threat_contact1 = models.CharField(max_length=15,blank=True, null=True)
    threat_contact2 = models.CharField(max_length=15,blank=True, null=True)
    threat_contact3 = models.CharField(max_length=15,blank=True, null=True)
    nearest_police_station_location = models.CharField(max_length=255,blank=True, null=True)

    current_location = models.CharField(max_length=255, blank=True, null=True)
    safety_status = models.BooleanField(default=True)
    safety_word = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.user.email} - Safety Profile'
