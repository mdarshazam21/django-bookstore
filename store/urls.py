from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("book/<int:pk>/", views.book_detail, name="book_detail"),
    path("cart/add/<int:pk>/", views.cart_add, name="cart_add"),
    path("cart/remove/<int:pk>/", views.cart_remove, name="cart_remove"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("checkout/", views.order_create, name="order_create"),
    path('orders/', views.order_history, name='order_history'),
]
