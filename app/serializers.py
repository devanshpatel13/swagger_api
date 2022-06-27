from .models import *
from rest_framework import serializers

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields =['id','name', 'std']
    #
    # def get_serializer_class(self):
    #     if self.request.version == 'v1':
    #         return HomeSerializer
    #     return HomeSerializer




class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields =['id','name', 'std']