from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from myapp.models import Data
from myapp.serializers import DataSerializer
from rest_framework import viewsets
import json
from django.http import JsonResponse

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
#         serializer = DataSerializer(queryset, many=True)
# class DataView(APIView):

#     def get(self, *args, **kwargs):

#         return Response(serializer.data)


def publish_message(request):
    request_data = json.loads(request.body)
    serializer_class = DataSerializer

