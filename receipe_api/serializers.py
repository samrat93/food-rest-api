from dataclasses import field
from rest_framework import serializers
from  .models import Receipe


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe
        field = '__all__'