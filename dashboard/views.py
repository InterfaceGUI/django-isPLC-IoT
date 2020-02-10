from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


@login_required(login_url="/login/")
def editdash(request):
    return render(request, "pages/edit-dashboard.html")