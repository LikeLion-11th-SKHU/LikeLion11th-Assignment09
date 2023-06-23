from django import forms
from .models import JournalUseForm

class JournalForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = JournalUseForm
        fields = ['title', 'weather', 'content', 'image']