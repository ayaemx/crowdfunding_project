from django.urls import path
from . import views

urlpatterns = [
    # Example path (replace with your real view)
    path('', views.category_list, name='category-list'),
]
