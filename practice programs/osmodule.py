import os
print(os.getcwd())
def list_files_in_current_directory():
    current_dir = os.getcwd()
    files = [file for file in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, file))]
    print("Files in the current directory:")
    for file_name in files:
        print(file_name)
list_files_in_current_directory()
