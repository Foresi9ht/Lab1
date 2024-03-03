import string
import os

def generatefiles():
    try:
        for letter in string.ascii_uppercase:
            file_path = f'{letter}.txt'
            with open(file_path, 'w') as file:
                file.write(f'This is the content of file {file_path}')
            print(f"File '{file_path}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

"""def deletefiles():
    try:
        for letter in string.ascii_uppercase:
            file_path = f'{letter}.txt'
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")"""

generatefiles()
"""deletefiles()"""
