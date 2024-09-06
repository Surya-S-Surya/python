from django import forms
from .models import BusDetails


class TicketForm(forms.ModelForm):
    np=forms.IntegerField()
    class Meta:
        model=BusDetails
        field=['busno','d','np']
