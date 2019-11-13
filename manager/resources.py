from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import League, Team, Game


class TeamResource(resources.ModelResource):
    league = fields.Field(
        column_name='league',
        attribute='league',
        widget=ForeignKeyWidget(League, 'abbreviation'))

    class Meta:
        model = Team


class GameResource(resources.ModelResource):
    team = fields.Field(
        column_name='team',
        attribute='team',
        widget=ForeignKeyWidget(Team, 'abbreviation'))

    opponent = fields.Field(
        column_name='opponent',
        attribute='opponent',
        widget=ForeignKeyWidget(Team, 'abbreviation'))

    class Meta:
        model = Game
