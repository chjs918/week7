from django import forms
from .models import Game

class gameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title','writer', 'content', 'img']

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')