from django import forms
from .models import JournalUseForm

class JournalUseForm(forms.ModelForm):
    class Meta:
        model = JournalUseForm
        fields = ['title', 'date', 'weather', 'content', 'file', 'image']
        