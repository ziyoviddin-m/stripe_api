from django.shortcuts import render
from rest_framework import viewsets

from item.serializers import ItemSerializers

from item.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers


