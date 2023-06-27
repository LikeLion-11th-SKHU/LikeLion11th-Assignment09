from django import forms
from .models import JournalUseForm

class JournalForm(forms.ModelForm):
    class Meta:
        model = JournalUseForm
        fields = ['title', 'weather', 'journal', 'image']