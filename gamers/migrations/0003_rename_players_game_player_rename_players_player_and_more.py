# Generated by Django 4.0.4 on 2022-05-26 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamers', '0002_alter_players_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='players',
            new_name='player',
        ),
        migrations.RenameModel(
            old_name='Players',
            new_name='Player',
        ),
        migrations.CreateModel(
            name='Winners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamers.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamers.player')),
            ],
        ),
    ]
