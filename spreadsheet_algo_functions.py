import os

# for searching for a directory within a list of items. Returns false
# if directory with desired name is not found
def find_dir(dir, name):
    for item in dir:
        if not os.path.isfile(item) and item.casefold() == name.casefold():
            return True
    return False
