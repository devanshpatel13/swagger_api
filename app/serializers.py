from .models import *
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields =['id','name', 'std']
    #


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["name", "subj","phone"]