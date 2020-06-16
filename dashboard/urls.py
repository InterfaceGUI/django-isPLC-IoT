from django.views.generic import RedirectView
from django.urls import path, re_path, include
from .views import editdash, dashpage, Create_Control, ControlUpdateView, ControlDeleteView, index, device,HomePage
from avatar.views import change
urlpatterns = [
    # Matches any html file

    re_path(r'dashboard/edit', editdash, name='edit'),
    re_path(r'dash/', dashpage, name='dash'),
    path('SelectionControl', Create_Control.as_view(), name="CreateControl"),
    path('update/<int:pk>', ControlUpdateView.as_view(), name='update_Control'),
    path('delete/<int:pk>', ControlDeleteView.as_view(), name='delete_Control'),
    path('dashboard/', index, name='home'),
    path('', HomePage, name='homepage'),
    path('My_Device/', device, name='device'),
]
