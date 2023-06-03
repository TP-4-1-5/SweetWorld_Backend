from django.urls import path
from . import views
from .views import RegistrationView, LoginView, FavoritesView

urlpatterns = [
    path('registration', RegistrationView.as_view(), name='registration'),
    path('login', LoginView.as_view(), name='login'),
    path('getFavorites', FavoritesView.as_view(), name='getFavorites'),
]