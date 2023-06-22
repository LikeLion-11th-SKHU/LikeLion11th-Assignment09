from django import forms
from .models import ReviewUseForm

class ReviewForm(forms.ModelForm) :
    class Meta:
        model = ReviewUseForm
        fields = ['title','weather','content','picture']