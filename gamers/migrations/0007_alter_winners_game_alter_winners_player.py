# Generated by Django 4.0.4 on 2022-05-30 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0006_alter_game_pub_date_alter_player_discordid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winners',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamers.game'),
        ),
        migrations.AlterField(
            model_name='winners',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamers.player'),
        ),
    ]
