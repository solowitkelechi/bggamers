# Generated by Django 4.0.4 on 2022-05-27 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0004_alter_game_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={},
        ),
        migrations.RemoveField(
            model_name='player',
            name='position',
        ),
    ]
