from django import forms
from django.contrib.auth.models import User
from django import forms
from django.core.files.images import get_image_dimensions


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
