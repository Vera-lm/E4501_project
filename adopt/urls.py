from django.urls import path

from . import views

urlpatterns = [
        path('',views.homepage_view),
        path('map/',views.map_view),
        path('list/',views.list_sights),
        path('stats/',views.stats),
        path('add/',views.add_sights),
        path('update/<Unique_Squirrel_ID>/',views.update_sights),
        ]

