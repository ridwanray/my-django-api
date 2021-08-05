from django.urls import path
from .views import (NewDataCreate, AllDataInformation)


urlpatterns = [
    path('create/', NewDataCreate.as_view(), name="create_new_data"),
    path('all/', AllDataInformation.as_view(), name="all_data_listings"), 
]

