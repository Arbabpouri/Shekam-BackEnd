# Generated by Django 5.1.3 on 2025-02-08 11:50

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نوشیدنی')),
            ],
            options={
                'verbose_name': 'نوشیدنی',
                'verbose_name_plural': 'نوشیدنی ها',
                'db_table': 'drinks',
            },
        ),
        migrations.CreateModel(
            name='FoodPromise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='وعده غذایی')),
            ],
            options={
                'verbose_name': 'وعده غذایی',
                'verbose_name_plural': 'وعده های غذایی',
                'db_table': 'food_promise',
            },
        ),
        migrations.CreateModel(
            name='FoodTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نوع غذا')),
                ('price', models.FloatField(verbose_name='قیمت غذا')),
            ],
            options={
                'verbose_name': 'نوع غذا',
                'verbose_name_plural': 'انواع غذا',
                'db_table': 'foods_type',
            },
        ),
        migrations.CreateModel(
            name='SideDishesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام مخلفات')),
            ],
            options={
                'verbose_name': 'مخلفات',
                'verbose_name_plural': 'مخلفات',
                'db_table': 'side_dishes',
            },
        ),
        migrations.CreateModel(
            name='FoodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50, verbose_name='نام غذا')),
                ('rating', models.FloatField(default=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='امتیاز')),
                ('drink', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drink', to='food_app.drinkmodel', verbose_name='نوشیدنی')),
                ('food_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_type', to='food_app.foodtypemodel', verbose_name='نوع غذا')),
                ('side_dishes', models.ManyToManyField(blank=True, to='food_app.sidedishesmodel', verbose_name='مخلفات')),
            ],
            options={
                'verbose_name': 'غذا',
                'verbose_name_plural': 'غذا ها',
                'db_table': 'foods',
            },
        ),
    ]
