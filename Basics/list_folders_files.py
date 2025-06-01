import os
# This script lists files in multiple directories specified by the user.
folders = input("Please provide list of folders with spaces - ").split()
 
for folder in folders:
    print(f"*** Files present under {folder} directory ***")
    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print(f"Folder '{folder}' does not exist.")
        continue
    except PermissionError:
        print(f"Permission denied for folder '{folder}'.")
        continue
    for file in files:
        print(file)


# This code snippet prompts the user to enter a list of folder names, separated by spaces. 
# The input function will read as a single string and then split into a list of folder names using the split() method, which by default splits on whitespace. 
# This allows the user to specify multiple folders in one line.
# The code then iterates over each folder name in the list. For each folder, it prints a message indicating that it will list the files under that directory. 
# It attempts to retrieve the list of files in the folder using os.listdir(folder). 
# If the folder does not exist, a FileNotFoundError is caught, and an error message is printed. 
# If the program does not have permission to access the folder, a PermissionError is caught, and a different error message is shown.
# In both error cases, the loop continues to the next folder without crashing.
# If the folder is accessible and exists, the code iterates through the list of files returned by os.listdir() and prints each file name.
# This provides a simple way for users to see the contents of multiple directories in one run. 
# One thing to note is that the code assumes the os module has already been imported; otherwise, it will raise a NameError. 
# Also, folder names containing spaces will not be handled correctly, as the split will break them into separate entries.