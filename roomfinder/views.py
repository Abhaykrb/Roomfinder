from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import finded_rooms
from django.contrib.gis.measure import D 
from django.contrib.gis.geos import Point

#Shows directly homepage
class base(TemplateView):
    template_name= 'base.html'

def rooms_datasets(request):    
   rooms = serialize('geojson', finded_rooms.objects.all())  
   return HttpResponse(rooms,content_type='json')

def showrooms(request):
    return render(request,'index.html')

def helpp(request):
    return render(request,'help.html')
          
    
