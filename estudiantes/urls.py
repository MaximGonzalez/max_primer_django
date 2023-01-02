from django.urls import path
from estudiantes.views import *

urlpatterns = [
    path('saludar/', saludar)
]