from django.contrib import admin
from .models import Location, Starbase, Item, MarketEntry

admin.site.register(Location)
admin.site.register(Starbase)
admin.site.register(Item)
admin.site.register(MarketEntry)

