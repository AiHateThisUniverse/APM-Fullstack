# Generated by Django 5.0.1 on 2024-02-05 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_user_groups_remove_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='userprofile',
            new_name='userprofile_created_c80f69_idx',
            old_name='apm_userpro_created_45c704_idx',
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='userprofile',
        ),
    ]
