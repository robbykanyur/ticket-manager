from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select/league', views.select_league, name='select_league'),
]
