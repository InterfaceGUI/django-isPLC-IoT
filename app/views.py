# Create your views here.

from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import UserProfile , UserLineForm,LineNsettingForm,LineUsettingForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import LineModel,LineSettingsModel
from django.contrib import messages

@login_required(login_url="/login/")
def UserLineSetting(request):
   
    if request.method == "POST":
        try:
            instance = LineModel.objects.get(author=request.user)
            form = UserLineForm(request.POST or None ,instance=instance)
        except LineModel.DoesNotExist:
                form = UserLineForm(request.POST)

        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
            messages.success(request, 'Success Upload Line Channel Access Token(CAT)!')
    
    lsList = list()
    try: 
        LSMobj = LineSettingsModel.objects.filter(author=request.user)
        for x in LSMobj:
            lsList.append(x)
    except LineSettingsModel.DoesNotExist :
        lsList = list()

    form = UserLineForm()
    return render(request,"pages/setting.html",{"form":form,'lineSetting':lsList})

class Create_LineSetting(BSModalCreateView):
    form_class = LineNsettingForm
    template_name = 'pages/CreatLineSetting.html'
    success_message = 'Success! New Setting was created.'
    success_url = reverse_lazy('LineSettings')

class LineSettingUpdateView(BSModalUpdateView):
    model = LineSettingsModel
    template_name = 'pages/update_LineSetting.html'
    form_class = LineUsettingForm
    success_message = 'Success! LineSetting was updated.'
    success_url = reverse_lazy('LineSettings')

class LineSettingDeleteView(BSModalDeleteView): 
    model = LineSettingsModel
    template_name = 'pages/delete_lineSerring.html'
    success_message = 'Success! LineSetting was deleted.'
    success_url = reverse_lazy('LineSettings')


@login_required(login_url="/login/")
def userProfileView(request):
    isUpdate = False
    if request.method == "POST":

        instance = get_object_or_404(User, id=request.user.id)
        form = UserProfile(request.POST or None , instance=instance)
        print('')
        if form.is_valid():
            form.save()
            isUpdate = True

    else:  # 当正常访问时

        if hasattr(request.user, '_wrapped') and hasattr(request.user, '_setup'):
            if request.user._wrapped.__class__ == object: 
                request.user._setup()
            user = vars(request.user._wrapped)

        form = UserProfile(user)

    return render(request, "user/user-profile.html", {"form": form,'isUpdate' : isUpdate})


@login_required(login_url="/login/") 
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

def handler404(request):
    response = render(request, 'pages/logoutError-404.html')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, 'pages/logoutError-500.html')
    response.status_code = 500
    return response

