from django import forms
from django.contrib.auth.models import User

class UserProfile(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "username",                
                "class"       : "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class"       : "form-control"
            }
        ))
    class Meta:
        model = User
        fields = ('username','email')
        