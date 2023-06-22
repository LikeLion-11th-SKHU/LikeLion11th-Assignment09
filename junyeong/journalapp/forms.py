from django import forms
from .models import Journal

class Journal(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['title', 'weather', 'body', 'image']