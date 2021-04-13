from django.urls import path

from . import views

urlpatterns = [
        path('adopt/',views.map,name = 'map'),
        ]

