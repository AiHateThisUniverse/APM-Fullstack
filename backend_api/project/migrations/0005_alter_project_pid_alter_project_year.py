# Generated by Django 5.0.1 on 2024-02-02 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_am_alter_project_amount_exc_tax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pid',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='year',
            field=models.IntegerField(),
        ),
    ]
