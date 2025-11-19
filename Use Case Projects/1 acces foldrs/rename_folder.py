import os

# Define the directory path
directory_path = r"R:\good pics"

# Check if the directory exists
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    # List all folders in the directory
    folders = [f for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]
    
    # Sort folders to ensure consistent ordering
    folders.sort()

    # Rename folders by adding numbers
    for index, folder in enumerate(folders, start=1):
        # Create the new folder name
        new_name = f"{index}_{folder}"
        # Full paths for the old and new folder names
        old_folder_path = os.path.join(directory_path, folder)
        new_folder_path = os.path.join(directory_path, new_name)
        
        # Rename the folder
        os.rename(old_folder_path, new_folder_path)
        print(f"Renamed '{folder}' to '{new_name}'")
else:
    print(f"The directory '{directory_path}' does not exist or is not accessible.")
