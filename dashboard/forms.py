from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm


from .models import control


def takeindex4sort(elem):
    return elem.index
    
class ControlForm(BSModalForm): 

    def __init__(self, *args, **kwargs):
        user_id = kwargs['request'].user.id
        #['request']['user']['id']

        super(ControlForm, self).__init__(*args, **kwargs)

        controls = control.objects.all() #取出全部合集
        uLControls = list()
        for c in controls:
            if c.uid == user_id:
                uLControls.append(c)
        uLControls.sort(key=takeindex4sort)
        self.initial['index'] = uLControls[-1].index + 1

        uid = user_id 
        self.initial['uid'] = uid
        self.initial['Text'] = '-'
        self.fields['uid'].disabled = True
        self.fields['index'].disabled = True

    class Meta:
        model = control
        exclude = ['timestamp',]

class UControlForm(BSModalForm): 

    def __init__(self, *args, **kwargs):
        #['request']['user']['id']
        super(UControlForm, self).__init__(*args, **kwargs)

        self.fields['uid'].disabled = True
        
    class Meta:
        model = control
        exclude = ['timestamp',]
