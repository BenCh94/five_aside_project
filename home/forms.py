from django import forms
from .models import Player

class NewPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'image')

