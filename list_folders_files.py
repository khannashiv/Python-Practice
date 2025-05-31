import os

# To get list of folders from user input
# Example: folders = ['folder1', 'folder2', 'folder3']
# print(folders)

folders = input("Please provide list of folders with spaces - ").split()
 
for folder in folders:
    print(f"Files present under {folder} directory.")
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


