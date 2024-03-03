def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return -1
    except Exception as e:
        print(f"Error: {e}")
        return -1

file_path = 'C:/Directories/3file.txt'
lines = count_lines(file_path)

if lines != -1:
    print(f"The number of lines in '{file_path}' is: {lines}")
