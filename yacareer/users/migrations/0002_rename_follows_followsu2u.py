# Generated by Django 3.2.16 on 2022-12-20 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follows',
            new_name='FollowsU2U',
        ),
    ]
