from rest_framework import serializers
from .models import Property  # or whatever model you want to expose

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'