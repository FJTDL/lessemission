# Generated by Django 4.0.3 on 2022-07-01 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('emission_calculator', '0008_identity_remove_carbonscore_parent_delete_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Identity',
            new_name='CustomUser',
        ),
    ]
