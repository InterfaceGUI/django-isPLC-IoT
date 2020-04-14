# Create your views here.

from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import UserProfile
from django.contrib.auth.models import User

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

