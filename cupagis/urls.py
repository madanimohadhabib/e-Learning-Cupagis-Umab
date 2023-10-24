from django.urls import path
from . import views

urlpatterns = [

    path('', views.liste_modules, name='liste_modules'),
    path('module/<int:module_id>-<str:nom_module>/', views.module_detail, name='module_detail'),
]
