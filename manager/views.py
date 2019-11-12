from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse('hello world')


def select_league(request):
    template = loader.get_template('manager/select_league.html')
    context = {}
    return HttpResponse(template.render(context, request))
