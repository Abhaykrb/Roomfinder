from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
# Create your models here.

class finded_rooms(models.Model):
    name=models.CharField(max_length=20)
    koordinate=models.PointField(srid=4326)
    room_rate=models.IntegerField()
    des=models.TextField() 
    objects = GeoManager()
    
def __unicode__(self):                #constructor
        return self.name
