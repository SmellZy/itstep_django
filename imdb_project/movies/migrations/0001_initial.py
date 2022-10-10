# Generated by Django 4.1.2 on 2022-10-10 22:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('date', models.DateField(null=True)),
                ('photo', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0, message='Min value shuld be less then 0'), django.core.validators.MaxValueValidator(10.0, message='Max value should be not higher then 10')])),
                ('genres', models.ManyToManyField(to='movies.genre')),
            ],
        ),
    ]
