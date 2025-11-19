import os
import cv2
from collections import defaultdict

# Function to detect faces in an image using OpenCV Haar cascades
def detect_faces(image_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return len(faces)

def rename_and_segregate_images_by_faces(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter out .jpg files
    jpg_files = [f for f in files if f.endswith('.jpg')]
    
    # Dictionary to store files by number of faces
    faces_dict = defaultdict(list)
    
    # Group files by number of faces
    for idx, filename in enumerate(jpg_files, 1):
        image_path = os.path.join(directory, filename)
        num_faces = detect_faces(image_path)
        faces_dict[num_faces].append(filename)
        
        # Calculate progress percentage
        progress = idx / len(jpg_files) * 100
        print(f"Progress: {progress:.2f}%\r", end="")
    
    print("\nProcessing complete. Moving files...")
    
    # Create directories based on number of faces if they don't exist
    for num_faces, file_list in faces_dict.items():
        faces_folder = os.path.join(directory, f"{num_faces}_faces")
        if not os.path.exists(faces_folder):
            os.makedirs(faces_folder)
        
        # Move files to the appropriate folder
        for filename in file_list:
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(faces_folder, filename)
            os.rename(old_path, new_path)
            print(f"Moved: {old_path} to {new_path}")
    
    print("All files have been segregated based on the number of faces detected.")

# Example usage
rename_and_segregate_images_by_faces(r'R:\recycle pics')
