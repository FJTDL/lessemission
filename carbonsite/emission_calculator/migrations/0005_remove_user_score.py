# Generated by Django 4.0.3 on 2022-07-01 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emission_calculator', '0004_alter_user_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='score',
        ),
    ]