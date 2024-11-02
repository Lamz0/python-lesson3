try:
    with open ("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("THe file was not found")

# this function here attempts to read and handles the case where the file does not exist
# by catching a FileNotFoundError