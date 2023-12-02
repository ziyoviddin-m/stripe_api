from http import HTTPStatus
from django.shortcuts import render
import stripe
from django.conf import settings
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponseRedirect

from item.models import Item, Order
from item.serializers import ItemSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY


# API View
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class SuccessTemplateView(TemplateView):
    template_name = 'item/success.html'


class BuyApi(APIView):
    def get(self, request, item_id):
        item = Item.objects.get(pk=item_id)
        line_items = []
        
        product = {
            'price': item.stripe_item_price_id,
            'quantity': 1
        }
        line_items.append(product)
        session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('item:success')),
        )
        return Response({'session_id': session.id})
        

class ItemApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item/item.html'

    def get(self, request, item_id):
        item = Item.objects.get(pk=item_id)
        serializer = ItemSerializer(item)
        return Response({'serializer': serializer, 'item': item})
    

class OrderCreateApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item/order.html'
    
    def get(self, request):
        orders = Order.objects.all()
        return Response({'orders': orders})

    def post(self, request):
        orders = Order.objects.all()
        line_items = []
        
        for order in orders:
            item = {
                'price': order.items.stripe_item_price_id,
                'quantity': 1
            }
            line_items.append(item)

        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('item:success')),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)








