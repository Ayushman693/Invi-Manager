# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-05 02:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=400)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='UploadedDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('storage_path', models.CharField(max_length=1000)),
                ('status', models.IntegerField(choices=[(100, 'Uploaded'), (200, 'UnderReview'), (300, 'Digitized')], default=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExtractedDoc',
            fields=[
                ('uploaded_doc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='docs_management.UploadedDoc')),
                ('invoice_number', models.CharField(default='', max_length=100)),
                ('summary', models.CharField(max_length=1000)),
            ],
        ),
    ]