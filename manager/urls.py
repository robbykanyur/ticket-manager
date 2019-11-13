from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.select_league, name='add_league'),
    path('add/<str:league>/', views.select_team, name='select_team'),
    path('schedule/<str:league>/<str:team>/', views.show_games, name='show_games'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/register', views.register, name='register'),
]
