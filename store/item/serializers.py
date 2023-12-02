from rest_framework import serializers

from item.models import Item, Order


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


