from rest_framework import serializers
from .models import demomodel


class demoSerializer(serializers.ModelSerializer):

    class Meta:
        model = demomodel
        fields = '__all__'