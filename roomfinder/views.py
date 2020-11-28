from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import getroom
#from django.contrib.gis.measure import D 
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

def userinput(request):
    if request.method == 'POST' :  
        name = request.POST.get('namee')#accessing 'name'value entered by using in userinput.html   
        coordinates = request.POST.get('koordinatee')
        coords = coordinates.split(',')
        point = Point(float(coords[0]), float(coords[1]))
        phonenumber=request.POST.get('phnumm')
        flooravailable=request.POST.get('flooorr')
        availableroomsno=request.POST.get('roomsnumm')
        rentratee = request.POST.get('roomratee')
        store = getroom(namee=name, koordinatee=point,phnumm=phonenumber,flooorr=flooravailable,roomsnumm=availableroomsno, roomratee=rentratee)#inserting userinput value into models field
        store.save()# saves these values of store in getroom table database directly
        return redirect('base')#takes to homepage
    else:
        # GET, generate unbound (blank) form
        return render(request,'userinput.html')
          
    
