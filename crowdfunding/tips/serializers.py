from rest_framework import serializers
from django.apps import apps

class TipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('tips.Tip')
        fields = '__all__'
