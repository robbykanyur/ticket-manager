from django import forms
from .models import Team

class AddTicketsForm(forms.Form):
    tickets_name = forms.CharField(label='Team name', max_length=100)
    tickets_password = forms.CharField(label='Team password', max_length=100, widget=forms.PasswordInput())
    class Meta:
        model = Team
