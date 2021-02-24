import json

from django.shortcuts import render
from django.views import View
from drf_yasg.utils import swagger_auto_schema


class TestView(View):

    @staticmethod
    def get(request):
        pass

    @staticmethod
    def post(request):
        pass
