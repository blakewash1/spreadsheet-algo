import os, os.path as op, spreadsheet_algo_functions as saf, time
from tqdm import tqdm

# get name of webpage source from user input
user_folder = input("Enter name of webpage source (html): ")

# check if user html exists in the "put html_here" directory. 
# If not, exit program
dir_path = op.join(os.getcwd(), "put_html_here")
dir_list = os.listdir(dir_path)

if saf.find_item_in_dir(dir_list, user_folder, False):
    print("Webpage found.")
    time.sleep(1.5)

else:
    print("Webpage not found. Exiting...") 

# add a short delay
time.sleep(2)