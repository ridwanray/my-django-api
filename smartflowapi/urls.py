from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('adminhidden/', admin.site.urls),
    path('auth/', include('myauth.urls')),
    path('api/',include('datainformation.urls')),
]
