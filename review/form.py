from django import forms
from .models import Userreview

class Reviewform(forms.ModelForm):
    class Meta:
        model = Userreview
        fields = ['image', 'title', 'body']

class Editform(forms.ModelForm):
    class Meta:
        model = Userreview
        fields = ['title', 'image', 'menu', 'body']