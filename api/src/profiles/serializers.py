from .models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    customer_name=serializers.CharField(source='user.username')
    class Meta:
        model=Customer
        fields=['id','country_code','phone_no','user','customer_name']
