import os
import shutil
import datetime

def get_month_name(modification_time):
    """Return the month name for the given timestamp."""
    return datetime.datetime.fromtimestamp(modification_time).strftime('%B')

def organize_files_by_month(folder_path):
    """Organize files in the given folder by their creation month."""
    if not os.path.isdir(folder_path):
        print(f"The provided path '{folder_path}' is not a valid directory.")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            print(f"file_path", file_path)
            modification_time = os.path.getmtime(file_path)
            month_name = get_month_name(modification_time)
            month_folder = os.path.join(folder_path, month_name)
            
            if not os.path.exists(month_folder):
                os.makedirs(month_folder)

            shutil.move(file_path, os.path.join(month_folder, filename))
            print(f"Moved: {filename} to {month_name} folder.")

def main():
    """Main function to run the file organization script."""
    folder_path = input("Enter the path of the folder to organize: ").strip()

    if not folder_path:
        print("No path provided. Exiting.")
        return

    organize_files_by_month(folder_path)
    print("File organization completed.")

if __name__ == "__main__":
    main()
