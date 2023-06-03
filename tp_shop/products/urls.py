from django.urls import path
from . import views
from .views import ProductView, ProductListView, ProductListWithCategoryView, AddToFavoritesView, \
    DeleteFromFavoritesView, ProductListWithNameView, GetProductComments

urlpatterns = [
    path('getproduct', ProductView.as_view(), name='getproduct'),
    path('getproductlist', ProductListView.as_view(), name='getproductlist'),
    path('getproductlistwithcategory', ProductListWithCategoryView.as_view(), name="getproductlistwithcategory"),
    path('addtofavorite', AddToFavoritesView.as_view(), name='addtofavorite'),
    path('deletefromfavorite', DeleteFromFavoritesView.as_view(), name='deletefromravorite'),
    path('getcommentslist', GetProductComments.as_view(), name='getcommentslist'),
    path('getproductlistwithname', ProductListWithNameView.as_view(), name='getproductlistwithname'),
]