from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select', views.select_league, name='select_league'),
    path('select/nfl', views.select_team, name='select_team'),
]
