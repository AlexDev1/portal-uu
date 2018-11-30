from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    # adm_changeusr = UserSerializer(many=False, read_only=True)
    class Meta:
        model = News
        fields = '__all__'
