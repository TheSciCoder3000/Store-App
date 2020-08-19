from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='store-home'),
    path('deactivate_btn/', views.deactivate_btn, name='deactivate-btn'),
    path('store/', views.store, name='store-store'),
    path('store/admin_orders', views.orders_to_admin, name='admin-orders'),
    path('store/admin_requests', views.requests_to_admin, name='admin-requests'),
    path('update_item/', views.update_item, name='update_item'),
]
