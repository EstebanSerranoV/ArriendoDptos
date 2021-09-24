from django.db.models import fields
from .models import Producto
from rest_framework import serializers
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'