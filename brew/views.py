from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Coffee
from .models import Snack
from .serializers import CoffeeSerializer
from .serializers import SnackSerializer

# Create your views here.
@api_view(['GET', 'POST']) 
def get_or_create_coffee(request): # View to create a new coffee
    if request.method == 'GET':
        coffees = Coffee.objects.all()
        serializer = CoffeeSerializer(coffees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CoffeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST']) # View to create a new snack
def get_or_create_snack(request):
    if request.method == 'GET':
        snacks = Snack.objects.all()
        serializer = SnackSerializer(snacks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SnackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET']) # View to get a coffee by ID
def get_coffee_by_id(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    serializer = CoffeeSerializer(coffee)
    return Response(serializer.data)

@api_view(['GET']) # View to get a snack by ID
def get_snack_by_id(request, pk):
    snack = get_object_or_404(Snack, pk=pk)
    serializer = SnackSerializer(snack)
    return Response(serializer.data)


