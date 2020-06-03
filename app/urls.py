from django.views.generic import RedirectView
from django.urls import path, re_path,include
from app import views
from .views import userProfileView, UserLineSetting,Create_LineSetting,LineSettingUpdateView,LineSettingDeleteView

urlpatterns = [
    # Matches any html file 
    re_path('user-profile.html', userProfileView, name='user'),
    re_path("setting.html",UserLineSetting,name="LineSettings"),
    path('NewSetting', Create_LineSetting.as_view(), name="CreateLineSetting"),
    path('updateLineSetting/<int:pk>', LineSettingUpdateView.as_view(), name="updateLineSetting"),
    path('deleteLineSetting/<int:pk>', LineSettingDeleteView.as_view(), name="deleteLineSetting"),
    re_path(r'^.*\.html', views.pages, name='pages'),
    #re_path(r'dashboard/',RedirectView.as_view(url='/')),
    # The home page 
    
]
