from django.contrib import admin
from . import models
# Register your models here.


class WeekMealPlanModelAdmin(admin.ModelAdmin):

    search_fields = ('year', 'number_of_week')
    list_display = ('pk', 'year', 'number_of_week')


class DailyMealPlanModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'day', 'food_promise', 'food', 'week')
    search_fields = ('day', 'food_promise', 'week')


admin.site.register(models.WeekMealPlanModel, WeekMealPlanModelAdmin)
admin.site.register(models.DailyMealPlanModel, DailyMealPlanModelAdmin)
