import os
from collections import defaultdict

def rename_images(directory, start_index=1):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter out .jpg files
    jpg_files = [f for f in files if f.endswith( 'avif')]
    
    # Sort the files by size
    jpg_files.sort(key=lambda f: os.path.getsize(os.path.join(directory, f)))
    
    # Dictionary to store files by size
    size_dict = defaultdict(list)
    
    # Group files by size
    for filename in jpg_files:
        file_size = os.path.getsize(os.path.join(directory, filename))
        size_dict[file_size].append(filename)
    
    # Identify duplicates and keep unique files
    unique_files = []
    for file_list in size_dict.values():
        unique_files.append(file_list[0])  # Keep one file from each size group
        for duplicate_file in file_list[1:]:
            os.remove(os.path.join(directory, duplicate_file))
            print(f"Removed duplicate: {duplicate_file}")

    # Rename each unique file starting from the specified index
    for index, filename in enumerate(unique_files, start=start_index):
        new_name = f"{index}.jpg"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} to {new_path}")

# Example usage
rename_images(r'R:\good pics', start_index=100)
