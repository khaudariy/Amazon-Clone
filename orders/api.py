from rest_framework import generics
import datetime
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
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


class ApplyCouponAPI(generics.GenericAPIView):

          def post(self,request,*args,**kwargs):
                 user = User.objects.get(username=self.kwargs['username'])   
                 coupon = get_object_or_404(Coupon,code=request.data['coupon_code'])
                 delivery_fee=Delivery.objects.last().fee
                 cart = Cart.objects.get(user=user,status='Inprogress')
                 if coupon and coupon.quantity > 0:
                    today_date=datetime.datetime.today().date()
                    if today_date >= coupon.start_date and today_date <=coupon.end_date:
                        coupon_vale =round(cart.cart_total / 100*coupon.discount,2)
                        sub_total = cart.cart_total - coupon_vale
                        total = sub_total+delivery_fee

                        cart.coupon=coupon
                        cart.total_with_coupon=sub_total
                        cart.save()
                        coupon.quantity-=1
                        coupon.save()
                        return Response({'message':'coupon was applied sucessfuly'})
                    else:
                        return Response({'message':'coupon is invalid or expired'})
                 return Response({'message':'coupon not found'})
                          