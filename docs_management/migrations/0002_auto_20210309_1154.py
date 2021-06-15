# Generated by Django 3.1.7 on 2021-03-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadeddoc',
            name='status',
            field=models.IntegerField(choices=[(1, 'Uploaded'), (2, 'UnderReview'), (3, 'Digitized')], default=1),
        ),
    ]
