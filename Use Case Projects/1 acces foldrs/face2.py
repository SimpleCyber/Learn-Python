import os
import cv2
import numpy as np
import face_recognition
from sklearn.cluster import DBSCAN
import pickle

# Function to detect and extract face encodings from an image using face_recognition
def detect_and_extract_faces(image_path):
    img = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)
    return face_encodings

def update_face_model(directory, model_path='face_model.pkl'):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter out .jpg files
    jpg_files = [f for f in files if f.endswith('.jpg')]
    
    # Load existing model if it exists
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            face_features, filenames = pickle.load(f)
    else:
        face_features = []
        filenames = []
    
    # Extract and store face encodings
    for idx, filename in enumerate(jpg_files, 1):
        image_path = os.path.join(directory, filename)
        face_encodings = detect_and_extract_faces(image_path)
        for encoding in face_encodings:
            face_features.append(encoding)
            filenames.append(filename)
        
        # Calculate progress percentage
        progress = idx / len(jpg_files) * 100
        print(f"Progress: {progress:.2f}%\r", end="")
    
    print("\nProcessing complete. Clustering faces...")
    
    # Save updated model
    with open(model_path, 'wb') as f:
        pickle.dump((face_features, filenames), f)
    
    return face_features, filenames

def segregate_images_by_face_similarity(directory, face_features, filenames):
    # Cluster faces based on similarity
    face_features = np.array(face_features)
    clustering = DBSCAN(eps=0.6, min_samples=1, metric='euclidean').fit(face_features)
    
    # Create directories based on cluster labels
    for cluster_label in set(clustering.labels_):
        cluster_folder = os.path.join(directory, f"cluster_{cluster_label}")
        if not os.path.exists(cluster_folder):
            os.makedirs(cluster_folder)
    
    # Move files to the appropriate folder
    for idx, label in enumerate(clustering.labels_):
        filename = filenames[idx]
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, f"cluster_{label}", filename)
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"Moved: {old_path} to {new_path}")
    
    print("All files have been segregated based on face similarity.")

# Example usage
directory = r'R:\recycle pics'
model_path = 'face_model.pkl'

# Update face model with new images
face_features, filenames = update_face_model(directory, model_path)

# Segregate images by face similarity
segregate_images_by_face_similarity(directory, face_features, filenames)
