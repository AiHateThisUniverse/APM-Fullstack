# Generated by Django 5.0.1 on 2024-01-31 06:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('pic_phone', models.CharField(max_length=20)),
                ('pic_email', models.EmailField(max_length=254)),
                ('pic_title', models.CharField(max_length=255)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='client_logos/')),
                ('company_size', models.CharField(choices=[('besar', 'Besar'), ('sedang', 'Sedang'), ('kecil', 'Kecil')], default='sedang', max_length=255)),
                ('company_address', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_person_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('company_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('date_joined', models.DateField()),
                ('status', models.CharField(choices=[('aktif', 'Aktif'), ('tidak aktif', 'TIdak Aktif')], default='aktif', max_length=20)),
                ('last_activity', models.DateTimeField()),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'client',
                'db_table': 'apm_client',
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['-created_at'], name='apm_client_created_422f30_idx')],
            },
        ),
    ]
