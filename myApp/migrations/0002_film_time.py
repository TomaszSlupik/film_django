# Generated by Django 4.0.1 on 2023-10-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='time',
            field=models.IntegerField(null=True),
        ),
    ]
