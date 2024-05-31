from django.contrib import admin
from .models import PersonalProfile

class PersonalProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone_number', 'city', 'state', 'blood_group')
    search_fields = ('user__username', 'first_name', 'last_name', 'email', 'phone_number', 'city', 'state', 'blood_group')
    list_filter = ('city', 'state', 'blood_group')

admin.site.register(PersonalProfile, PersonalProfileAdmin)
