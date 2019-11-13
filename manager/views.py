from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import League, Team, Game


def index(request):
    return render(request, 'manager/home.html')


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('index')

    f = UserCreationForm()
    context = {'form': f}
    return render(request, 'registration/register.html', context)


@login_required
def select_league(request):
    leagues = League.objects.all()
    context = {'leagues': leagues}
    return render(request, 'manager/select_league.html', context)


@login_required
def select_team(request, league):
    league = League.objects.get(abbreviation=league.upper())
    teams = Team.objects.filter(league__abbreviation__contains=league)
    sorted_teams = sorted(teams, key=lambda t: t.display_name())
    context = {'teams': sorted_teams, 'league': league}
    return render(request, 'manager/select_team.html', context)


@login_required
def show_games(request, league, team):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'manager/show_games.html', context)
