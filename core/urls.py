"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from isplcAPI import views
from rest_framework.authtoken.views import obtain_auth_token
from core import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'isplcs', views.isplcViewSet)
router.register(r'devices', views.devicesViewSet)
router.register(r'token2auther', views.TokenAuthorView, basename='T4A')
router.register(r'GetControlContext', views.ControlContextView, basename='ControlContext')

urlpatterns = [
    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path("", include("app.urls")),
    path("", include("dashboard.urls")),
    re_path(r'^api/', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),
    path('avatar/', include('avatar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 