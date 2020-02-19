from django import forms
from .models import Userreview

class Reviewform(forms.ModelForm):
    class Meta:
        model = Userreview
        fields = ['image', 'title', 'body']
        # fields = '__all__' models.py에서 지정한 모든 필드?를 사용하고 싶을 때 사용.