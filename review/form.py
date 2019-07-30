from django import forms
from .models import Userreview

class Reviewform(forms.ModelForm):
    class Meta:
        model = Userreview
        fields = ['image', 'title', 'body']