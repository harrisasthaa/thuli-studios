from rest_framework import serializers
from .models import UserRequest, Dress, Recommendation

class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = ['user_id', 'image', 'preferences', 'created_at']

class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dress
        fields = ['name', 'description', 'image_url']

class RecommendationSerializer(serializers.ModelSerializer):
    user_request = UserRequestSerializer()
    recommended_dress = DressSerializer()

    class Meta:
        model = Recommendation
        fields = ['user_request', 'recommended_dress', 'created_at']
