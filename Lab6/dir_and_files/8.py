import os
import stat

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            else:
                print(f"Error: You don't have permission to delete '{file_path}'.")
        else:
            print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

file_path = 'C:/Directories/4file.txt'
delete_file(file_path)
