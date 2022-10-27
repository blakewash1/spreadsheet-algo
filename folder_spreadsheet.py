import os, os.path as op, spreadsheet_algo_functions as saf, time
from tqdm import tqdm

# get name of folder from user input
user_folder = input("Enter folder name: ")

# check if user folder exists in the "put folder_here" directory. 
# If not, exit program
dir_path = op.join(os.getcwd(), "put_folder_here")

if saf.find_dir(dir_path, user_folder):
    # join user folder to current directory path
    dir_path = op.join(dir_path, user_folder)

    # create a list of the sub-directories wihin the user folder
    sub_dir_list = [f for f in os.listdir(dir_path) if not op.isfile(f)]

    # check to see if list has content. If not, exit program
    if sub_dir_list:
        print("Folder found.")
        time.sleep(1.5)

        # creating progress bar
        increment = 100 / len(sub_dir_list)
        progress_bar = tqdm(total=100, desc="Parsing folders", colour="blue", ncols=150)
        
        # create dictionary for create_spreadsheet() function
        folder_dict = {}
        sub_dir_list.sort()
        for dir in sub_dir_list:
            # getting the directory's contents
            contents = os.listdir(op.join(dir_path, dir))
            contents.sort()
            # add folder-name/contents pair to dictionary
            folder_dict[dir] = contents
            # updating the progress bar
            time.sleep(0.1)
            progress_bar.update(increment)

        progress_bar.close()
        saf.create_spreadsheet(user_folder, folder_dict)
    
    else:
        print("There are no sub-folders within selected folder. Exiting...")
    
else:
    print("Folder not found. Exiting...") 

# add a short delay
time.sleep(2)


