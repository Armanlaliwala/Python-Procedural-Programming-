import os

folder_path = r"C:\Users\arman\Desktop\Silver_oak_uni\Python\2024\exercise\photos"

# List all files in the folder
files = os.listdir(folder_path)

# Filter only image files
image_files = [file for file in files if file.endswith(".jpg")]

# Sort the image files to maintain order
image_files.sort()

# Rename the files
for i, file_name in enumerate(image_files, start=1):
    file_path = os.path.join(folder_path, file_name)
    new_file_name = f"photo{i}.jpg"
    new_file_path = os.path.join(folder_path, new_file_name)
    os.rename(file_path, new_file_path)

print("All images have been renamed.")
