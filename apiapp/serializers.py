from rest_framework import serializers
from .models import user

class ItemSerializer(serializers.ModelSerializer):
      class Meta:
          model = user
          fields = '__all__'
  