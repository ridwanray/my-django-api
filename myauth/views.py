from .serializers import MyTokenObtainPairSerializer,UserSerializerWithToken,RegisterSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from accounts.models import CustomUser
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import (api_view, authentication_classes, 
permission_classes)
from rest_framework.response import Response
from allauth.account.forms import ResetPasswordForm
from django.contrib.auth.hashers import make_password



@api_view(['POST'])
@permission_classes([AllowAny,])
def registerUser(request):
    data = request.data
    try:
        user = CustomUser.objects.create(
        email=data['email'],
        password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'Email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
