# Generated by Django 4.0.3 on 2022-06-22 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enfuego', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pointtable',
            options={'ordering': ['-points', '-goaldifference', '-goalsscored']},
        ),
    ]