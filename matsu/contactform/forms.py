from django import forms

class MatsuContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    organization = forms.CharField()
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'span5'}))
