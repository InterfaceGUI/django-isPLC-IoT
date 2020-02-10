from django.views.generic import RedirectView
from django.urls import path, re_path,include
from .views import editdash
urlpatterns = [
    # Matches any html file 

    re_path(r'dashboard/edit',editdash, name='edit'),

]
