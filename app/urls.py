from django.views.generic import RedirectView
from django.urls import path, re_path,include
from app import views
from .views import userProfileView
urlpatterns = [
    # Matches any html file 
    
    re_path('user-profile.html', userProfileView, name='user'),
    re_path(r'^.*\.html', views.pages, name='pages'),
    #re_path(r'dashboard/',RedirectView.as_view(url='/')),
    # The home page 
    
]
