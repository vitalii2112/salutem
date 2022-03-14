from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', login_required(views.EditingPatient.as_view()), name='medicalcard'),
]