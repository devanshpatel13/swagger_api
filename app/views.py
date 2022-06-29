
from django.shortcuts import render
# from requests import Response
from rest_framework import viewsets
from rest_framework.schemas import openapi
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import *
from .models import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    swagger_tags =['Rrrrrrr']
    # # metadata_class = APIRootMetadata



    @swagger_auto_schema(tags=['my student tag'])
    def list(self, request, *args, **kwargs):
        return super(StudentViewSet, self).list(request, args, kwargs)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    swagger_tags = ["Teacher"]










