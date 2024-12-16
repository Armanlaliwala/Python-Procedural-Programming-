import os
import shutil

def organize_files(folder_path):
    folders = {
        "Images": [".jpeg", ".jpg", ".gif", ".png", ".bmp"],
        "Documents": [".txt", ".docx", ".doc", ".pdf", ".xlsx", ".xls", ".pptx", ".ppt"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
        "Audios": [".mp3", ".wav", ".ogg", ".flac"],
        "Archives": [".zip", ".rar", ".7z", ".tar.gz"],
        "Executables": [".exe", ".msi"],
        "Scripts": [".py", ".sh", ".bat"],
        "Others": []  # Default folder for other file types
    }

    for folder_name in folders:
        dest_folder = os.path.join(folder_path, folder_name)
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

    for file_name in os.listdir(folder_path):
        source_file = os.path.join(folder_path, file_name)
        if os.path.isfile(source_file):
            file_extension = os.path.splitext(file_name)[1]
            for folder_name, extensions in folders.items():
                if file_extension.lower() in extensions:
                    dest_folder = os.path.join(folder_path, folder_name)
                    dest_file = os.path.join(dest_folder, file_name)
                    if not os.path.exists(dest_file):
                        try:
                            shutil.move(source_file, dest_folder)
                            print(f"Moved {file_name} to {dest_folder}")
                        except Exception as e:
                            print(f"Error moving {file_name}: {e}")
                    else:
                        print(f"File {file_name} already exists in {dest_folder}")
                    break

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder to organize: ")
    organize_files(folder_path)
    print("Files organized successfully.")
