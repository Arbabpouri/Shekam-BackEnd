from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class FoodType(models.Model):
    name = models.CharField(max_length=300, verbose_name="نوع غذا")
    price = models.FloatField(verbose_name="قیمت غذا")

    class Meta:
        db_table = 'foods_type'
        verbose_name = 'نوع غذا'
        verbose_name_plural = 'انواع غذا'

    def __str__(self):
        return f"{self.name}={self.price}"
    

class SideDishes(models.Model):
    name = models.CharField(max_length=300, verbose_name="نام مخلفات")

    class Meta:
        db_table = 'side_dishes'
        verbose_name = 'مخلفات'
        verbose_name_plural = 'مخلفات'

    def __str__(self):
        return self.name
    

class Drink(models.Model):
    name = models.CharField(max_length=300, verbose_name="نوشیدنی")

    class Meta:
        db_table = 'drinks'
        verbose_name = 'نوشیدنی'
        verbose_name_plural = 'نوشیدنی ها'

    def __str__(self):
        return self.name


class Food(models.Model):
    food_name = models.CharField(max_length=50, verbose_name="نام غذا")
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name="food_type", verbose_name="نوع غذا", null=False)
    side_dishes = models.ManyToManyField(SideDishes, verbose_name="مخلفات", blank=True)
    drink = models.ForeignKey(Drink, on_delete=models.SET_NULL, verbose_name="نوشیدنی", related_name="drink", null=True, blank=True)
    rating = models.FloatField(validators=(MinValueValidator(0), MaxValueValidator(5)), verbose_name="امتیاز", default=5)

    class Meta:
        db_table = 'foods'
        verbose_name = 'غذا'
        verbose_name_plural = 'غذا ها'

    def __str__(self):
        return f"{self.food_name}|{self.food_type}"
