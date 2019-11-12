from django.http import HttpResponse
from django.template import loader

from .models import League, Team


def index(request):
    return HttpResponse('hello world')


def select_league(request):
    template = loader.get_template('manager/select_league.html')
    leagues = League.objects.all()
    context = {'leagues': leagues}
    return HttpResponse(template.render(context, request))


def select_team(request):
    template = loader.get_template('manager/select_team.html')
    teams = Team.objects.filter(league__abbreviation__contains="NFL")
    sorted_teams = sorted(teams, key=lambda t: t.display_name())
    context = {'teams': sorted_teams}
    return HttpResponse(template.render(context, request))
