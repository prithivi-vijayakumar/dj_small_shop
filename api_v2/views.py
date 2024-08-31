from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from backend.models import Category

from api_v2.serializers import CategorySerializer


# Create your views here.
class CategoryListView(generics.ListAPIView):
    queryset = Category. objects.all()
    serializer_class =  CategorySerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            "data" : serializer.data
        }
        return Response(data)