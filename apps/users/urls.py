from django.urls import path
from . import views

urlpatterns = [
    # Example:
    path('', views.user_home, name='user-home'),
]
