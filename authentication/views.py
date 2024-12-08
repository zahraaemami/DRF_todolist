from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework .response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status

from .serializers import UserSerializer
from .models import User



class RegisterView(GenericAPIView) :
    
    serializer_class = UserSerializer
    
    def post (self , request) :
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response (serializer.data , status = 200)