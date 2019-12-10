from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import sightings
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .forms import sightingsform
import json

def all_squirrels(request):
    squirrels = sightings.objects.all()
    context = {
            'squirrels':squirrels
            }
    return render(request,'sightings/all.html',context)

def update(request,squirrel_id):
    sight = sightings.objects.get(Unique_Squirrel_ID = squirrel_id)
    if request.method == 'POST':
        form = sightingsform (request.POST, instance = sight)
        
        if form.is_valid():
           sight=form.save()
           sight.save()
           return redirect(f'/sightings/')
    else:
        form = sightingsform(instance=sight)
    context={
                'form':form,
        }
    return render(request,'sightings/update_form.html',context)

def add(request):
    if request.method == 'POST':
        form = sightingsform(request.POST)
        if form.is_valid():
            form.save()
        return redirect(f'/sightings/')
    else:
        form = sightingsform()
    context = {'form':form,}
    return render(request,'sightings/squirrel_form.html',context)

def stats(request):
    Total_Sightings=sightings.objects.all().count()
    Sightings_Night=sightings.objects.filter(Shift='PM').count()
    Sightings_Adult=sightings.objects.filter(Age='Adult').count()
    Sightings_Running=sightings.objects.filter(Running='True').count()
    Sightings_Black=sightings.objects.filter(Primary_Fur_Color='Black').count()

    context = {
              'Total_Sightings': Total_Sightings,
              'Sightings_Night': Sightings_Night,
              'Sightings_Adult':Sightings_Adult,
              'Sightings_Running':Sightings_Running,
              'Sightings_Black':Sightings_Black,
              }
    return render(request, 'sightings/stats.html',context)

def map(request):
    sight = sightings.objects.order_by('?')[:100]
    context = {
            'sight':sight
            }
    return render(request,'sightings/map.html',context)
