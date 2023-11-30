from rest_framework import serializers

from item.models import Item


class ItemSerializers(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'

