"""tp_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
import users, productscategory, products, comments
from django.views.static import serve
from . import settings
from .yasg import urlpatterns1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('productscategory/', include('productscategory.urls')),
    path('products/', include('products.urls')),
    path('comments/', include('comments.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
urlpatterns += urlpatterns1
