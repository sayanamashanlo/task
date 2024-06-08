from rest_framework import serializers
from .models import Task
from rest_framework.exceptions import ValidationError


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'