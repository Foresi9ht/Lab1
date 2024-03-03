def list_to_file(file_path, input_list):
    try:
        with open(file_path, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"Successfully wrote the list to '{file_path}'.")
    except Exception as e:
        print(f"Error: {e}")

file_path = 'C:/Directories/3file.txt'
your_list = ["Ola", "Amigo", "que", "porfavor?"]

list_to_file(file_path, your_list)
