import os
import shutil

# Define file type categories
docext = ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx']
imgext = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.avif']
vidext = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.mpg', '.mpeg']

categories = ['Documents', 'Images', 'Videos', 'Others']

def organize_folder(target_folder):
    try:
        # Create subfolders if they don't exist
        for category in categories:
            folder_path = os.path.join(target_folder, category)
            try:
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
            except Exception as e:
                print(f"Error creating folder '{folder_path}': {e}")

        # Loop through all items in the target folder
        for item in os.listdir(target_folder):
            item_path = os.path.join(target_folder, item)

            # Skip directories
            if os.path.isdir(item_path):
                continue

            # Get file extension
            _, extension = os.path.splitext(item)
            extension = extension.lower()

            # Decide destination folder
            if extension in docext:
                destination_folder = os.path.join(target_folder, 'Documents')
            elif extension in imgext:
                destination_folder = os.path.join(target_folder, 'Images')
            elif extension in vidext:
                destination_folder = os.path.join(target_folder, 'Videos')
            else:
                destination_folder = os.path.join(target_folder, 'Others')

            # Move the file
            try:
                new_path = os.path.join(destination_folder, item)
                shutil.move(item_path, new_path)
                print(f"Moved '{item}' to '{destination_folder}'")
            except Exception as e:
                print(f"Failed to move '{item}': {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    try:
        folder = input("Enter the path of the folder to organize: ").strip()
        if os.path.exists(folder):
            organize_folder(folder)
            print("\nOrganization complete!")
        else:
            print("Error: The specified folder does not exist.")
    except Exception as e:
        print(f"An error occurred while processing the folder: {e}")
