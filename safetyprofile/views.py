from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import SafetyProfile
from .serializers import SafetyProfileSerializer
import json
from django.contrib.auth.models import User


class SafetyProfileViewSet(viewsets.ModelViewSet):
    queryset = SafetyProfile.objects.all()
    serializer_class = SafetyProfileSerializer

    @action(detail=False, methods=['post'], url_path='update-location')
    def update_location(self, request):
        user = request.user
        current_location = request.data.get('current_location')

        if not current_location:
            return Response({"error": "Current location is required"}, status=status.HTTP_400_BAD_REQUEST)

        safety_profile, created = SafetyProfile.objects.get_or_create(user=user)
        safety_profile.current_location = current_location
        safety_profile.save()

        return Response({"status": "Location updated"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='trigger-emergency')
    def trigger_emergency(self, request):
        user = request.user
        safety_word = request.data.get('safety_word')

        if not safety_word:
            return Response({"error": "Safety word is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            safety_profile = SafetyProfile.objects.get(user=user)
        except SafetyProfile.DoesNotExist:
            return Response({"error": "Safety profile not found"}, status=status.HTTP_404_NOT_FOUND)

        safety_profile.safety_word = safety_word
        safety_profile.safety_status = False
        safety_profile.save()

        # Add your logic to send location and details to the contacts
        # For example, you could use Twilio to send SMS or another service for emails

        return Response({"status": "Emergency triggered"}, status=status.HTTP_200_OK)
def update_safety_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        status = data.get('safety_status')

        try:
            profile = SafetyProfile.objects.get(user_id=user_id)
            profile.safety_status = status
            profile.save()
            return JsonResponse({'status': 'success', 'message': 'Safety status updated successfully'})
        except SafetyProfile.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Profile not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)