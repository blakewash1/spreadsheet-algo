import os

# for searching for a directory within a list of items. Returns false
# if directory with desired name is not found
def find_dir(dir, name):
    for item in dir:
        if not os.path.isfile(item) and item.casefold() == name.casefold():
            return True
    return False

# for listing out the contents of the sub-directory in alpha-numeric order
def list_contents(dir_path, dir):
    print("\n" + dir)
    contents = os.listdir(op.join(dir_path, dir))
    contents.sort()
    for content in contents:
        print(content)
