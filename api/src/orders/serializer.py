from rest_framework import serializers
from .models.models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id','item_name','amount',
                  'customer','created_at','updated_at']
        extra_kwargs = {
            'customer':{'write_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
