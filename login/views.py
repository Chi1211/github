from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserLoginSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
from django.conf import settings

class UserLogin(APIView):
    permission_classes=([permissions.AllowAny,])

    def post(self, request):
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user=serializer.validated_data['user']
        login(request, user)
        refresh=RefreshToken.for_user(user)
        respone={
            "username":user.username,
            "password":user.password,
            "status_code": 200,
            # "refresh": str(refresh),
            "token": str(refresh.access_token),
            
        }

        return Response(respone, status=200)
        # if user: 
        #     jwt_token =jwt.encode({'id':user.id}, settings.JWT_SECRET_KEY)
        #     data={'user':serializer.data, 'token':jwt_token }
        #     login(request, user)
        #     return Response(data, status=200)
        # return Response({'detail':'error'}, status=400)
