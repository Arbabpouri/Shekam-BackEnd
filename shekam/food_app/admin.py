from django.contrib import admin
from . import models

# Register your models here.

class FoodModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'type', 'drink', 'rating', 'get_side_dishes')
    search_fields = ('pk', 'name', 'type', 'rating')
    sortable_by = 'rating'

    def get_side_dishes(self, obj):
        return ", ".join([side_dish.name for side_dish in obj.side_dishes.all()])
    get_side_dishes.short_description = 'مخلفات'


class FoodTypeModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price')
    search_fields = ('price', )


class SideDishesModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('pk', 'name')


class DrinkModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('pk', 'name')


class FoodPromiseModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('pk', 'name')


admin.site.register(models.FoodModel, FoodModelAdmin)
admin.site.register(models.FoodTypeModel, FoodTypeModelAdmin)
admin.site.register(models.SideDishesModel, SideDishesModelAdmin)
admin.site.register(models.DrinkModel, DrinkModelAdmin)
admin.site.register(models.FoodPromiseModel, FoodPromiseModelAdmin)
