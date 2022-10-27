import os, os.path as op, spreadsheet_algo_functions as saf, time
from tqdm import tqdm
from bs4 import BeautifulSoup as bs

# get name of webpage source from user input
user_file = input("Enter name of webpage source (html): ")

# check if user html exists in the "put html_here" directory. 
# If not, exit program
dir_path = op.join(os.getcwd(), "put_html_here")
proper_file = saf.find_file(dir_path, user_file)

if proper_file != "nope":
    print("Webpage found.")
    time.sleep(1.5)

    

   # with open()



else:
    print("Webpage not found. Exiting...") 

# add a short delay
time.sleep(2)