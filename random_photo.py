import os
import random

photo_directory = "photo"

def get_path(child_directory, file_name):
    current_dir = os.getcwd()
    # Navigate to the parent directory
    file_path = os.path.join(current_dir, child_directory, file_name)
    return file_path



def get_file_names(directory):
    file_names = []
    for file_name in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file_name)):
            file_names.append(file_name)
    return file_names

def generate_random_integer(count):
    random_integer = random.randint(0, count - 1)
    return random_integer

def get_random_photo():
    files = get_file_names(photo_directory)
    return get_path(photo_directory, files[generate_random_integer(len(files))])


# print(get_random_photo())