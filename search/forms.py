from django import forms
from .models import Advertisment

class AdForm(forms.ModelForm):
    class Meta:
        model = Advertisment
        fields = ('name', 'description', 'capacity', 'conditions', 'image', 'date_created')
