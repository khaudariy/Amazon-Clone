from rest_framework import generics

from django.contrib.auth.models import User


from .serializers import CartDetailSerializer,CartSerializer,OrderDetailSerializer,OrderSerializer
from .models import Order,OrderDetail,Cart,CartDetail,Coupon
from products.models import Product
from settings.models import Delivery


class OrderListAPI(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_queryset(self):
        queryset = super(OrderListAPI,self).get_queryset()
        user = User.objects.get(username=self.kwargs['username'])
        queryset =queryset.filter(user=user)
        return super().get_queryset()
    
class OrderDeetailAPI(generics.RetrieveAPIView):
        serializer_class = OrderSerializer
        queryset = Order.objects.all()