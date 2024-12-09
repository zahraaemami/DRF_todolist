from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework .response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from django.contrib import auth
from .utils import generate_token
from .serializers import UserSerializer ,LoginSerializer
from .models import User
import jwt
#from django.contrib.auth.models import authentication


class RegisterView(GenericAPIView) :
    
    serializer_class = UserSerializer
    
    def post (self , request) :
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response (serializer.data , status =status.HTTP_201_CREATED)
    
    
class LoginView(GenericAPIView) :
    
    serializer_class = LoginSerializer

    def post (self , request) :
        data = request.data
        username = data.get('email' ,'')
        password = data.get('password','')
        user = auth.authenticate(username = username , password = password)
        if user :
            serializer = LoginSerializer(user)
            return Response(serializer.data , status =status.HTTP_200_OK)
        return Response({"massage":'try again '}, status = status.HTTP_401_UNAUTHORIZED)