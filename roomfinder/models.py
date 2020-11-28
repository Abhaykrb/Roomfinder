from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
# Create your models here.
class getroom(models.Model):
    namee=models.CharField(max_length=20)
    koordinatee=models.PointField(srid=4326,geography=True)
    phnumm=models.BigIntegerField()
    flooorr=models.CharField(max_length=16)
    roomsnumm=models.IntegerField()
    roomratee=models.IntegerField()
    objects = GeoManager()
    
def __unicode__(self):                #constructor
        return self.phnumm


