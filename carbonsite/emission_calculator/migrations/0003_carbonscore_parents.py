# Generated by Django 4.0.3 on 2022-07-01 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emission_calculator', '0002_alter_user_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='carbonscore',
            name='parents',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
