from django.urls import path
from . import views

urlpatterns = [
    path('getproduct', views.getproduct, name='getproduct'),
    path('getproductlist', views.getproductlist, name='getproductlist'),
    path('getproductlistwithcategory', views.getproductlistwithcategory, name="getproductlistwithcategory"),
]
