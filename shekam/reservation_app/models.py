from django.db import models
from food_app.models import FoodModel, FoodPromiseModel
import jdatetime
# Create your models here.


class Days:
    DAYS = (
        ('شنبه', 'شنبه'),
        ('یکشنبه', 'یکشنبه'),
        ('دوشنبه', 'دوشنبه'),
        ('سه شنبه', 'سه شنبه'),
        ('چهارشنبه', 'چهارشنبه'),
        ('پنجشنبه', 'پنجشنبه'),
        ('جمعه', 'جمعه'),
    )


class WeekMealPlanModel(models.Model):
    
    year = models.IntegerField(verbose_name='سال', default=jdatetime.datetime.now().year)
    number_of_week = models.IntegerField(verbose_name='شماره هفته در سال', default=jdatetime.datetime.today().isocalendar()[1])

    class Meta:
        db_table = 'week_meal_plan'
        verbose_name = 'برنامه هفتگی',
        verbose_name_plural = 'برنامه های هفتگی'
    
    def __str__(self):
        return f"هفته : {self.number_of_week} در سال {self.year}"
    
    def save(self, *args, **kwargs):

        if not WeekMealPlanModel.objects.filter(year=self.year, number_of_week=self.number_of_week).exists():
            return super().save(*args, **kwargs)
    
    
class DailyMealPlanModel(models.Model):
    day = models.CharField(max_length=50, choices=Days().DAYS, verbose_name="روز هفته")
    food_promise = models.ForeignKey(FoodPromiseModel, on_delete=models.CASCADE, related_name='food_promise', verbose_name='زمان وعده غذایی')
    food = models.ForeignKey(FoodModel, on_delete=models.CASCADE, related_name='food_model', verbose_name="غذا")
    week = models.ForeignKey(WeekMealPlanModel, on_delete=models.CASCADE, related_name='week', verbose_name='برنامه هفته')

    
    class Meta:
        db_table = 'dayli_meal_plan'
        verbose_name = 'وعده غذایی'
        verbose_name_plural = 'وعده های غذایی'


    def __str__(self):
        return f"{self.day} - {self.food.name} - {self.food_promise.name} - ({self.week.year} _ {self.week.number_of_week})"

