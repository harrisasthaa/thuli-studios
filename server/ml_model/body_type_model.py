from keras.models import load_model
import numpy as np
import cv2

# Load the pre-trained CNN model for body type classification
model = load_model('model_weights/body_type_cnn.h5')

def classify_body_type(image_path):
    image = cv2.imread(image_path)
    image_resized = cv2.resize(image, (128, 128))  # Resize to model input size
    image_array = np.array(image_resized) / 255.0  # Normalize the image
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

    prediction = model.predict(image_array)
    class_idx = np.argmax(prediction)
    
    # Assuming classes are ['Rectangle', 'Pear', 'Hourglass', 'Inverted Triangle']
    body_types = ['Rectangle', 'Pear', 'Hourglass', 'Inverted Triangle']
    predicted_body_type = body_types[class_idx]

    return predicted_body_type

# Example usage:
# body_type = classify_body_type("uploads/sample_image.jpg")
# print(f"Predicted Body Type: {body_type}")
