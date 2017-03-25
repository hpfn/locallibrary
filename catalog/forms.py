from django import forms
from .models import Language

class SelectBook(forms.Form):
    language = forms.CharField()
    #topic = forms.CharField()

#    class Meta:
#        model = Language
#        fields = ['language']

