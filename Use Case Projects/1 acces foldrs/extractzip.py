import os
import zipfile

# Directory containing the zip files
zip_dir = r'R:\nepal'

# Iterate through all files in the directory
for filename in os.listdir(zip_dir):
    if filename.endswith('.zip'):
        # Construct the full file path
        file_path = os.path.join(zip_dir, filename)
        
        # Open the zip file
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            # Extract all the contents into the same directory
            zip_ref.extractall(zip_dir)
        
        print(f'Extracted {filename}')

print('All zip files have been extracted.')
