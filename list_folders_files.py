import os

folders = input("Please provide list of folders with spaces - ").split()
 
# To get list of folders from user input
# Example: folders = ['folder1', 'folder2', 'folder3']
# print(folders)

for folder in folders:
    # print(folder)
    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print(f"Folder '{folder}' does not exist.")
        continue
    for file in files:
        print("Printing files in folder:", folder)
        print(file)


