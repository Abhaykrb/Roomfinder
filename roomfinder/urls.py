from django.conf.urls import include 
from .views import base,rooms_datasets,showrooms,helpp,userinput
from django.urls import path
#from .models import finded_rooms

urlpatterns= [
   
    path('', base.as_view(), name = 'base'),
    path('findrooms', rooms_datasets, name="roomsfound"), 
    path('showrooms', showrooms, name='showrooms'),
    path('helpp', helpp, name='helpp'),
    path('userinput', userinput, name='userinput'),
    ]
