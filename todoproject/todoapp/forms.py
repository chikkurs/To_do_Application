from django import forms
from .models import Todo
class Todoupdate(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['task','priority','date']