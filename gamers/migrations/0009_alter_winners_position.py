# Generated by Django 4.0.4 on 2022-05-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0008_alter_winners_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winners',
            name='position',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
