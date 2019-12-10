from django.urls import path
from . import views
from django.conf.urls import url
from .views import all_squirrels,add

urlpatterns = [
        path('sightings/',views.all_squirrels),
        path('Unique_Squirrel_ID', views.update),
        path('sightings/add/',views.add,name='add'),
        path('sightings/stats/',views.stats,name='stats'),
        path('map/',views.map,name='map'),
]
