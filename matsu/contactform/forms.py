from django import forms

class MatsuContactForm(forms.Form):
    name = forms.CharField(max_length=200, error_messages={'required' : 'Please provide your name.'})
    organization = forms.CharField(error_messages={'required' : 'Please provide your organization or university.'})
    sender = forms.EmailField(error_messages={'required' : 'Please provide your email.'})
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'span5'}), error_messages={'required' : 'Please share your thoughts about the site.'})
