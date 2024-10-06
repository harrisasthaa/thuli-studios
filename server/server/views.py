from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from dress_recommender_app.models import UserRequest, Dress, Recommendation
from dress_recommender_app.serializers import RecommendationSerializer, UserRequestSerializer
import os

@api_view(['POST'])
def upload_image(request):
    if 'image' not in request.FILES or 'preferences' not in request.data:
        return Response({"error": "Please upload an image and provide preferences"}, status=400)

    image = request.FILES['image']
    preferences = request.data['preferences']

    user_request = UserRequest.objects.create(
        image=image,
        preferences=preferences
    )

    # Save uploaded image temporarily and process it (image analysis and AI/ML code)
    temp_image_path = default_storage.save(image.name, ContentFile(image.read()))
    # ML processing code here (call model, analyze image, get recommendations)

    # Mock recommendation (Replace this with AI/ML-based recommendations)
    dress = Dress.objects.first()  # Mocking, getting the first dress for now
    Recommendation.objects.create(user_request=user_request, recommended_dress=dress)

    return Response({"message": "Image uploaded successfully"}, status=201)

@api_view(['GET'])
def get_recommendations(request):
    user_request_id = request.query_params.get('user_request_id', None)
    if not user_request_id:
        return Response({"error": "User request ID is required"}, status=400)

    recommendations = Recommendation.objects.filter(user_request__id=user_request_id)
    serializer = RecommendationSerializer(recommendations, many=True)

    return Response(serializer.data)
