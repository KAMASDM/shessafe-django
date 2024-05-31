from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import PersonalProfile
from .serializers import PersonalProfileSerializer

class PersonalProfileViewSet(viewsets.ModelViewSet):
    queryset = PersonalProfile.objects.all()
    serializer_class = PersonalProfileSerializer
