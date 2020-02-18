from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from bootstrap_modal_forms.generic import BSModalCreateView,BSModalUpdateView,BSModalDeleteView
from django.urls import reverse_lazy
from .forms import ControlForm ,UControlForm
from .models import control
# Create your views here.

def takeindex4sort(elem):
    return elem.index

@login_required(login_url="/login/")
def editdash(request):
    if request.method == "POST":        #如果是以POST的方式才處理
        mess = request.POST['itemindex'].split(',') #取得表單輸入資料
        
        for ic in mess:
            if ic == '':
                continue
            cpk = ic.split('=')[0]
            cindex = ic.split('=')[1]
            cc = control.objects.get(pk=cpk)
            cc.index = cindex
            cc.save()

    Ruid = request.user.id
    controls = control.objects.all() #取出全部合集
    uLControls = list()

    #過濾用戶的儀表
    for c in controls:
        if c.uid == Ruid:
            uLControls.append(c)

    uLControls.sort(key=takeindex4sort)

    return render(request, "pages/edit-dashboard.html",{'Controls': uLControls}) 
 
def dashpage(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('dash/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def index(request):
    
    Ruid = request.user.id
    controls = control.objects.all() #取出全部合集
    uLControls = list()
    for c in controls:
        if c.uid == Ruid:
            uLControls.append(c)

    uLControls.sort(key=takeindex4sort)
    return render(request, "index.html",{'Controls': uLControls })

class Create_Control(BSModalCreateView):
    form_class = ControlForm
    template_name = 'dash/SelectionControl.html'
    success_message = 'Success! Control was created.'
    success_url = reverse_lazy('edit')

class ControlUpdateView(BSModalUpdateView):
    model = control
    template_name = 'dash/update_Control.html'
    form_class = UControlForm
    success_message = 'Success! Control was updated.'
    success_url = reverse_lazy('edit')

class ControlDeleteView(BSModalDeleteView):
    model = control
    template_name = 'dash/delete_Control.html'
    success_message = 'Success! Control was deleted.'
    success_url = reverse_lazy('edit')
