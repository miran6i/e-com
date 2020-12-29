from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterView, ActivateView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<str:activation_code>/', ActivateView.as_view(), name='activate'),
    path('login/', LoginView.as_view()),
]