import os

def directories(path):
    print("Directories:")
    for dir_name in os.listdir(path):
        dir_path = os.path.join(path, dir_name)
        if os.path.isdir(dir_path):
            print(dir_name)

def files(path):
    print("\nFiles:")
    for file_name in os.listdir(path):
        file_path = os.path.join(path, file_name)
        if os.path.isfile(file_path):
            print(file_name)

def list_all(path):
    print("\nAll Directories and Files:")
    for item_name in os.listdir(path):
        item_path = os.path.join(path, item_name)
        print(item_name)

if __name__ == "__main__":
    target_path = "C:\Directories"
    directories(target_path)
    files(target_path)
    list_all(target_path)