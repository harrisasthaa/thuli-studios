from .facial_features_model import extract_facial_features
from .body_type_model import classify_body_type
import random

# Predefined Indian dresses based on body type and facial features
DRESS_RECOMMENDATIONS = {
    'Rectangle': ['Kurta with straight pants', 'Sari with minimal pleats'],
    'Pear': ['Anarkali suit', 'Lehenga with flared skirt'],
    'Hourglass': ['Sari with heavy draping', 'Fitted Kurta with palazzo'],
    'Inverted Triangle': ['Salwar Kameez', 'Sari with wide border'],
}

def recommend_dresses(image_path, user_preferences):
    # Extract facial features (for now we assume simpler logic)
    facial_features = extract_facial_features(image_path)

    # Classify body type
    body_type = classify_body_type(image_path)

    # Fetch recommendations based on body type
    recommended_dresses = DRESS_RECOMMENDATIONS.get(body_type, [])

    # Apply user preferences to filter or adjust recommendations (optional)
    if user_preferences:
        # Example: If the user prefers 'light colors', we might filter or adjust results.
        # For now, we're randomly selecting one dress.
        recommended_dress = random.choice(recommended_dresses)
    else:
        recommended_dress = random.choice(recommended_dresses)

    return {
        'body_type': body_type,
        'facial_features': 'Extracted',  # Replace with actual analysis later if needed
        'recommended_dress': recommended_dress
    }

# Example usage:
# recommendations = recommend_dresses("uploads/sample_image.jpg", user_preferences={'color': 'light'})
# print(recommendations)
