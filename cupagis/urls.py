from django.urls import path
from . import views

urlpatterns = [

    path('', views.liste_modules, name='liste_modules'),
]
