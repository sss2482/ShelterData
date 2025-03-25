from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import SDUser
# Create your views here.


# Custom token view to include user info
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = SDUser.objects.get(username=request.data['username'])
        response.data['user_id'] = user.id
        return response
