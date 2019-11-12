from django.contrib import admin

from .models import League, Team, Game

admin.site.register(League)
admin.site.register(Team)
admin.site.register(Game)
