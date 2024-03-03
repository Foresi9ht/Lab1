import os

def analyze_path(path):
    if os.path.exists(path):
        print(f"Path '{path}' exists.")

        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"Path '{path}' does not exist.")

path_to_analyze = "C:\Directories"
analyze_path(path_to_analyze)
