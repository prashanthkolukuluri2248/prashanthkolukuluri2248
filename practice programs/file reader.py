try:
    with open("test.txt","r") as file:
        content = file.read()
except FileExistsError:
    print("file path not found ")
except FileNotFoundError:
    print("file not found")
else:
    print("file read and has no errors")