from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.FoodModel)
admin.site.register(models.FoodTypeModel)
admin.site.register(models.SideDishesModel)
admin.site.register(models.DrinkModel)
admin.site.register(models.FoodPromise)
