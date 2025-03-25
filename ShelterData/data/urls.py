"""
URL configuration for ShelterData project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import MedicalFacilityListView, ResourceListView, ShelterListView, ShelterPostView, ShelterDetailView, VictimPostView, MissingPersonView, BestShelterView

urlpatterns = [
    path('medical_facilities/', MedicalFacilityListView.as_view(), name='medical_facilities'),
    path('resources/', ResourceListView.as_view(), name='resources'),
    path('shelters/', ShelterListView.as_view(), name='shelters'),
    path('new_shelter/', ShelterPostView.as_view(), name='shelterpost'),
    path('shelters/<int:id>/', ShelterDetailView.as_view(), name='shelter_detail'),
    path('best_shelter/', BestShelterView.as_view(), name='best_shelter'),
    path('new_victim/', VictimPostView.as_view(), name='new_victim'),
    path('missing_person/', MissingPersonView.as_view(), name='missing_person'),
    
]
