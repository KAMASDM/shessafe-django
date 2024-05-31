from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SafetyProfileViewSet

router = DefaultRouter()
router.register(r'safetyprofiles', SafetyProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
