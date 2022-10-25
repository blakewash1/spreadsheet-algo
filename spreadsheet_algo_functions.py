import os

# for searching for a directory within a list of items
def find_dir(dir, name):
    for item in dir:
        print(item)
        print(os.path.isfile(item)) 