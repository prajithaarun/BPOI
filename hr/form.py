from django import forms

class SubscribeForm(forms.Form):
        email=forms.EmailField()
        subject=forms.CharField(max_length=200)
        message=forms.CharField(max_length=200)