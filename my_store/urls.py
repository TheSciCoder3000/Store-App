from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('store/', views.store, name='store-store'),
]
