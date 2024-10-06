from django.urls import path
from . import views

urlpatterns = [
    path('upload_image/', views.upload_image, name='upload_image'),
    path('get_recommendations/', views.get_recommendations, name='get_recommendations'),
]
