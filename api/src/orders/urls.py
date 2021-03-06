from django.urls import path
from .views import (OrdersCreateApiView,
                    OrdersretriveAPiView,
                    OrdersListAPiView)



urlpatterns = [
    path('create/',OrdersCreateApiView.as_view(), name='orders_create'),
    path('retrieve/<int:pk>/',OrdersretriveAPiView.as_view(), name='orders_retrive'),
    path('list/',OrdersListAPiView.as_view(), name='orders_list'),
]
