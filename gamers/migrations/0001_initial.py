# Generated by Django 4.0.4 on 2022-05-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discordId', models.CharField(max_length=200)),
                ('position', models.IntegerField(max_length=20)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date hosted')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('host', models.CharField(max_length=100)),
                ('played', models.BooleanField(default=False)),
                ('players', models.ManyToManyField(blank=True, to='gamers.players')),
            ],
        ),
    ]
