# Generated by Django 3.2.16 on 2022-12-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20221219_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='фамилия'),
        ),
    ]
