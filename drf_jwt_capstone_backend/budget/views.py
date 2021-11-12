from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Food, Personal_Expenses, Insurance, Transportation, Housing, Utilities
from .serializers import FoodSerializer, PersonalExpensesSerializer, InsuranceSerializer, TransportationSerializer, HousingSerializer, UtilitiesSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_foods(request):
    foods = Food.objects.all()
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_foods(request):
    
    print(
        'User', f"{request.user.id} {request.user.email} {request.user.username}")
    
    if request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        foods = Food.objects.filter(user_id=request.user.id)
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_expenses(request):
    expenses = Personal_Expenses.objects.all()
    serializer = PersonalExpensesSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_expenses(request):
    
    print(
        'User', f"{request.user.id} {request.user.email} {request.user.username}")
    
    if request.method == 'POST':
        serializer = PersonalExpensesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        expenses = Personal_Expenses.objects.filter(user_id=request.user.id)
        serializer = PersonalExpensesSerializer(expenses, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_insurances(request):
    insurances = Insurance.objects.all()
    serializer = InsuranceSerializer(insurances, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_insurances(request):
    
    print(
        'User', f"{request.user.id} {request.user.email} {request.user.username}")
    
    if request.method == 'POST':
        serializer = InsuranceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        insurances = Insurance.objects.filter(user_id=request.user.id)
        serializer = InsuranceSerializer(insurances, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_transportations(request):
    transportations = Transportation.objects.all()
    serializer = TransportationSerializer(transportations, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_transportations(request):
    
    print(
        'User', f"{request.user.id} {request.user.email} {request.user.username}")
    
    if request.method == 'POST':
        serializer = TransportationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        transportations = Transportation.objects.filter(user_id=request.user.id)
        serializer = TransportationSerializer(transportations, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_houses(request):
    houses = Housing.objects.all()
    serializer = HousingSerializer(houses, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_houses(request):
    
    print(
        'User', f"{request.user.id} {request.user.email} {request.user.username}")
    
    if request.method == 'POST':
        serializer = HousingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        houses = Housing.objects.filter(user_id=request.user.id)
        serializer = HousingSerializer(houses, many=True)
        return Response(serializer.data)
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_utility(request):
    utility = Utilities.objects.all()
    serializer = UtilitiesSerializer(utility, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def user_utility(request):
    
    print(
        'User', f"{request.user.id} {request.user.email} {request.user.username}")
    
    if request.method == 'POST':
        serializer = UtilitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        utility = Utilities.objects.filter(user_id=request.user.id)
        serializer = UtilitiesSerializer(utility, many=True)
        return Response(serializer.data)