import os, os.path as op, spreadsheet_algo_functions as saf, time, xlsxwriter

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

        # create spreadsheet using xlsxwriter
        workbook = xlsxwriter.Workbook(user_folder +'.xlsx')
        
        sub_dir_list.sort()

        # iterate through list of sub-directories and its file contents
        for dir in sub_dir_list:
            saf.list_contents(dir_path, dir)

    else:
        print("There are no sub-folders within selected folder. Exiting...")
    
else:
    print("Folder not found. Exiting...") 

# add a short delay
time.sleep(1.5)


