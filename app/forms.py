from django import forms
from django.contrib.auth.models import User
from django import forms
from django.core.files.images import get_image_dimensions
from .models import LineModel,LineSettingsModel
from bootstrap_modal_forms.forms import BSModalForm

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

class UserLineForm(forms.ModelForm):
    LineToken = forms.CharField(
    widget=forms.TextInput(
        attrs={
            "placeholder" : "LineToken",                
            "class"       : "form-control"
        }
    ))

    class Meta:
        model = LineModel
        fields = ('LineToken',) 

class LineNsettingForm(BSModalForm): 

    def __init__(self, *args, **kwargs):
        author = kwargs['request'].user
        #['request']['user']['id']

        super(LineNsettingForm, self).__init__(*args, **kwargs)

        try:
            Setts = LineSettingsModel.objects.filter(author=author)
        except LineSettingsModel.DoesNotExist :
            Setts = []

        self.initial['author'] = author
        self.initial['Text'] = '-'

    class Meta:
        model = LineSettingsModel
        exclude = ['timestamp',]
        widgets = {
            'author': forms.HiddenInput(),
        }

class LineUsettingForm(BSModalForm): 

    def __init__(self, *args, **kwargs):
        #['request']['user']['id']
        super(LineUsettingForm, self).__init__(*args, **kwargs)

        
    class Meta:
        model = LineSettingsModel
        exclude = ['timestamp',]
        widgets = {
            'author': forms.HiddenInput(),
        }