
from django.contrib import admin
from .models import getroom
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class getroomAdmin(LeafletGeoAdmin):
 list_display=('namee','koordinatee' ,'phnumm','flooorr','roomsnumm','roomratee')#these things will be shown at /admin section    
admin.site.register(getroom,getroomAdmin)

