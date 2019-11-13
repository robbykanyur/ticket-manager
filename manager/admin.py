from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import League, Team, Game
from .resources import TeamResource, GameResource

admin.site.register(League)


@admin.register(Team)
class TeamAdmin(ImportExportModelAdmin):
    resource_class = TeamResource
    pass


@admin.register(Game)
class GameAdmin(ImportExportModelAdmin):
    resource_class = GameResource
    pass
