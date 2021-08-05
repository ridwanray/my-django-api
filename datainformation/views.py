from rest_framework import generics,permissions
from .models import DataInformation
from .serializers import DataInformationSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

class AllDataInformation(generics.ListAPIView):
    queryset = DataInformation.objects.all()
    serializer_class = DataInformationSerializer
    permission_classes = (IsAuthenticated,)


class NewDataCreate(generics.CreateAPIView):
    serializer_class = DataInformationSerializer
    permission_classes = (AllowAny,)
    

