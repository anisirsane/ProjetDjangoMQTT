from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from myapp.models import Data

class DataSerializer(ModelSerializer):

    class Meta:
        model = Data
        fields = ('temperature', 'humidity')



