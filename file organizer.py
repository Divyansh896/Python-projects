import os
import shutil


def organize_files(folder_path):
    # Create a dictionary to map file extensions to folder names
    extensions = {
        '.txt': 'TextFiles',
        '.doc': 'WordDocuments',
        '.pdf': 'PDFs',
        '.jpg': 'JPEGs',
        '.mp3': 'MP3s',
        '.py' : 'Pythonfiles',
        '.mp4' : 'videos'
        # Add more extensions and corresponding folder names as needed
    }

    # Iterate over all the files in the given folder
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Get the file extension
            _, file_ext = os.path.splitext(filename)

            # Check if the extension is present in the dictionary
            if file_ext.lower() in extensions:
                # Get the destination folder path based on the file extension
                dest_folder = os.path.join(folder_path, extensions[file_ext.lower()])

                # Create the destination folder if it doesn't exist
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                # Move the file to the destination folder
                shutil.move(os.path.join(folder_path, filename), os.path.join(dest_folder, filename))
                print(f"Moved {filename} to {dest_folder}")


# Provide the folder path where the files are located
folder_path = 'F:\\tester folder'

# Call the function to organize the files
organize_files(folder_path)
