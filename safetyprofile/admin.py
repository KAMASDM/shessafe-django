from django.contrib import admin
from .models import SafetyProfile

class SafetyProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'safety_status', 'current_location')
    search_fields = ('user__username', 'health_word_text', 'threat_word_text', 'current_location')
    list_filter = ('safety_status',)
    fieldsets = (
        (None, {
            'fields': ('user', 'current_location', 'safety_status', 'safety_word')
        }),
        ('Health Emergency Details', {
            'fields': (
                'health_word_audio', 'health_word_text',
                'health_contact1', 'health_contact2', 'health_contact3',
                'ambulance_contact', 'family_doctor_contact',
                'nearest_hospital_location'
            )
        }),
        ('Threat Emergency Details', {
            'fields': (
                'threat_word_audio', 'threat_word_text',
                'threat_contact1', 'threat_contact2', 'threat_contact3',
                'nearest_police_station_location'
            )
        }),
    )

admin.site.register(SafetyProfile, SafetyProfileAdmin)
