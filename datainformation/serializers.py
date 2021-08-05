from rest_framework import serializers
from .models import  DataInformation

class DataInformationSerializer(serializers.ModelSerializer):
    class Meta:     
        model = DataInformation
        fields = ['id','location','customer_name','amount_paid','volume_dispensed','complete_status',]
       