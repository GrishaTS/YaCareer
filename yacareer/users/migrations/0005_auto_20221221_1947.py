# Generated by Django 3.2.16 on 2022-12-21 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_usermedia_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followsu2u',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_follows', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='followsu2u',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_followed', to=settings.AUTH_USER_MODEL),
        ),
    ]
