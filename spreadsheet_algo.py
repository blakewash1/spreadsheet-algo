# The purpose of this script is to take in a folder as input, list out each sub-folder title as columns, then list out the 
# titles of each folders' contents as rows beneath aforementioned columns. All of this should be displayed on a spreadsheet,
# which is to be automatically downloaded at the end of the writing proccess.
# The following is a visual of how the spreadsheet should look:
#
#  FOLDER_1  | DATE | DIFFICULTY |  FOLDER_2  | DATE | DIFFICULTY | ...
# --------------------------------------------------------------------
#  CONTENT_1 |      |            | CONTENT_1  |      |            |
#  CONTENT_2 |      |            | CONTENT_2  |      |            |
#     ...    |      |            |    ...     |      |            |
# 
# This script was written with python version 3.9 in mind

import os, spreadsheet_algo_functions as saf, time

# get name of folder from user input
user_folder = input("Enter folder name: ")

# check if folder exists in current directory
dir_path = os.path.dirname(os.path.realpath(__file__))
top_dir_list = os.listdir(dir_path)
if saf.find_dir(top_dir_list, user_folder):
    print("Folder found. Generating spreadsheet...")
else:
    print("Folder not found") 

# add a short delay
time.sleep(1)
# for item in os.listdir(dir_path):
#     print(item)
#     print(os.path.isfile(item))

# for root, dirs, files in next(os.walk(dir_path))[1]:
#     for dir in dirs:
#         print(dir)


