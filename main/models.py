from django.db import models

BUY_OR_SELL = (
    (1, 'Buy'),
    (2, 'Sell'),
)

class Location(models.Model):
    system_id = models.IntegerField()
    system_name = models.TextField()
    cbody_id = models.IntegerField(null=True)
    cbody_name = models.TextField(null=True)

class Starbase(models.Model):
    starbase_id = models.IntegerField()
    aff = models.TextField(max_length=3)
    name = models.TextField()
    location = models.ForeignKey(Location)
    hiport = models.BooleanField()
    patch_price = models.IntegerField()
    dock_capacity = models.IntegerField()
    maint_complexes = models.IntegerField()

class Item(models.Model):
    item_id = models.IntegerField()
    name = models.TextField()
    lifeform = models.BooleanField(default=False)
    perish = models.BooleanField(default=False)

class MarketEntry(models.Model):
    starbase_id = models.ForeignKey(Starbase, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item)
    buy_or_sell = models.IntegerField(choices=BUY_OR_SELL)
    quant = models.IntegerField()
    price = models.FloatField()
