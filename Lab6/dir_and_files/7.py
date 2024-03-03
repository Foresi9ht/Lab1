def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
        
        with open(destination_file, 'w') as destination:
            destination.write(content)

        print(f"Contents of '{source_file}' successfully copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

source_file = 'C:/Directories/1file.txt'
destination_file = 'C:/Directories/2file.txt'

copy_file(source_file, destination_file)
