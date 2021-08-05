from django.urls import path
from myauth.views import MyTokenObtainPairView, RegisterView,registerUser
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('newregister/',  registerUser, name='newregisteration'),

]