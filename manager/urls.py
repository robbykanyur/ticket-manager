from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tickets/add', views.add_tickets, name='add_tickets'),
    path('tickets/create', views.create_tickets, name='create_tickets'),
    path('tickets/create/<str:league>/', views.select_team, name='select_team'),
    path('tickets/new/<str:league>/<str:team>/', views.new_tickets, name='new_tickets'),
    path('account/', include('django.contrib.auth.urls')),
    path('account/register', views.register, name='register'),
]
