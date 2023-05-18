from django.urls import path
from . import views

urlpatterns = [
    path('getproduct', views.getproduct, name='getproduct'),
    path('getproductlist', views.getproductlist, name='getproductlist'),
    path('addtofavorite', views.addtofavorite, name='addtofavorite'),
    path('deletefromfavorite', views.deletefromfavorite, name='deletefromravorite'),
    path('getproductlistwithcategory', views.getproductlistwithcategory, name="getproductlistwithcategory"),
]
