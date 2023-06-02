from django.urls import path
from . import views
from .views import ProductCategoryView

urlpatterns = [
    path('getproductscategorys', ProductCategoryView.as_view(), name='getproductscategorys'),
]