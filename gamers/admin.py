from django.contrib import admin

# Register your models here.

from .models import Player, Game,Winners

admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Winners)