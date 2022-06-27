
from django.shortcuts import render
# from requests import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import *
from .models import *
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
# Create your views here.

class CreateView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = HomeSerializer
    # metadata_class = APIRootMetadata
