from django.urls import path
from . import views

urlpatterns = [
    path('getproductscategorys', views.getproductscategorys, name='getproductscategorys'),
]