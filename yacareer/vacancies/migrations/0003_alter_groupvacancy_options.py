# Generated by Django 3.2.16 on 2022-12-23 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0002_rename_v_name_groupvacancy_vacancy_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='groupvacancy',
            options={'default_related_name': 'group_vacancy', 'ordering': ('id',), 'verbose_name': 'вакансия', 'verbose_name_plural': 'вакансии'},
        ),
    ]
