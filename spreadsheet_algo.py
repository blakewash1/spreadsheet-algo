import os, os.path as op, spreadsheet_algo_functions as saf, time

# get name of folder from user input
user_folder = input("Enter folder name: ")

# get the current directory, and check if user folder exists in it. If not, exit program
dir_path = op.join(os.getcwd(), "put_folder_here")
top_dir_list = os.listdir(dir_path)

if saf.find_dir(top_dir_list, user_folder):
    # join user folder to current directory path
    dir_path = op.join(dir_path, user_folder)

    # create a list of the sub-directories wihin the user folder
    sub_dir_list = [f for f in os.listdir(dir_path) if not op.isfile(f)]

    # check to see if list has content. If not, exit program
    if sub_dir_list:
        print("Folder found. Generating spreadsheet...")
        
        sub_dir_list.sort()
        saf.create_spreadsheet(user_folder, dir_path, sub_dir_list)
    
    else:
        print("There are no sub-folders within selected folder. Exiting...")
    
else:
    print("Folder not found. Exiting...") 

# add a short delay
time.sleep(1.5)


