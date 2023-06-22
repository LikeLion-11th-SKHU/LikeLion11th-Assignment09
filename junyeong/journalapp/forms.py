from django import forms
from .models import Journal

class Journalform(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'weather', 'body', 'image']