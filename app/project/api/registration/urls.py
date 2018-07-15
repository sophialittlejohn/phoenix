from django.urls import path

from project.api.registration.views import RegistrationView, RegistrationValidationView

app_name = 'registration'

urlpatterns = [
    path('', RegistrationView.as_view(), name='registration'),
    path('validate/', RegistrationValidationView.as_view(), name='registration_validation')
]
