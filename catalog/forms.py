from django import forms


class SelectBook(forms.Form):
    language = forms.CharField()
    # topic = forms.CharField()

#    class Meta:
#        model = Language
#        fields = ['language']
