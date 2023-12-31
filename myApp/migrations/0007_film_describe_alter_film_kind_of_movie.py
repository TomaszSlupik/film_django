# Generated by Django 4.0.1 on 2023-10-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_alter_film_kind_of_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='describe',
            field=models.TextField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='kind_of_movie',
            field=models.CharField(choices=[('Filmy akcji', 'Filmy akcji'), ('Fantastyczno-naukowy', 'Fantastyczno-naukowy'), ('Komedia romantyczna', 'Komedia romantyczna'), ('Komedia', 'Komedia'), ('Film dokumentalny', 'Film dokumentalny'), ('Horror', 'Horror'), ('Dramat', 'Dramat'), ('Fantastyczny', 'Fantastyczny')], max_length=50, null=True),
        ),
    ]
