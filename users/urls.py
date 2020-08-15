from django.urls import path
from my_store import views as store_views
from . import views as user_views

urlpatterns = [
    path('profile/', user_views.profile, name='profile'),
    path('profile/orders/<pk>/', store_views.OrderDetails.as_view(), name='user-order-detail'),
    path('profile/requests/<pk>/', store_views.OrderDetails.as_view(), name='user-request-detail'),
]
