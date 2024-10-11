import os

# Specify the path to the file
file_path = "temp_email.txt"

# Delete the file
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been deleted.")
else:
    print(f"{file_path} does not exist.")
