# Generated by Django 4.0 on 2022-10-25 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_musicstarr_bookstarr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rate',
        ),
    ]
