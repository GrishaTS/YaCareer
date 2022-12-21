# Generated by Django 3.2.16 on 2022-12-20 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='images/', verbose_name='фото')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='название')),
                ('about', models.CharField(blank=True, max_length=1024, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'группа',
                'verbose_name_plural': 'группы',
                'default_related_name': 'groups',
            },
        ),
        migrations.CreateModel(
            name='GroupMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='название')),
                ('file', models.FileField(upload_to='files/', verbose_name='файл')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'файл',
                'verbose_name_plural': 'файлы',
                'default_related_name': 'media',
            },
        ),
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_staff', models.BooleanField(default=False, verbose_name='персонал')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group', verbose_name='группа')),
            ],
        ),
    ]
