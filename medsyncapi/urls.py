from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from medsyncapi.app.views import PatientViewSet, DoctorViewSet, AppointmentViewSet, SpecialtiesViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'specialties', SpecialtiesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
