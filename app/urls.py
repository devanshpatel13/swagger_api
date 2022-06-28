from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework_swagger.views import get_swagger_view

from rest_framework import routers
#
router = routers.DefaultRouter()
router.register("swaggerapi", CreateView , basename = "create")

urlpatterns = [

    path('', include(router.urls)),


]