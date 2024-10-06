import cv2
import dlib
import numpy as np

# Load pre-trained model for face detection and landmark extraction
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('model_weights/shape_predictor_68_face_landmarks.dat')

def extract_facial_features(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    if len(faces) == 0:
        print("No face detected!")
        return None

    for face in faces:
        landmarks = predictor(gray, face)

        facial_features = np.zeros((68, 2), dtype='int')
        for i in range(0, 68):
            facial_features[i] = (landmarks.part(i).x, landmarks.part(i).y)

        return facial_features

# Example usage:
# features = extract_facial_features("uploads/sample_image.jpg")
# print(features)
