from rest_framework import serializers
from .models import Coffee
from .models import Snack

class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coffee
        fields=['id', 'type', 'temperature', 'caffeine_amount', 'price']
    
class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Snack
        fields=['id', 'type', 'product_name', 'price']