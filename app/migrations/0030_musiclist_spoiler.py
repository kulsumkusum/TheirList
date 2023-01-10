# Generated by Django 4.0 on 2022-10-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_booklist_spoiler'),
    ]

    operations = [
        migrations.AddField(
            model_name='musiclist',
            name='spoiler',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False, null=True),
        ),
    ]