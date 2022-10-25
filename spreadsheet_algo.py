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

import os, spreadsheet_algo_functions as saf

# get name of folder from user input
folder_name = input("Enter folder name: ")

# check if folder exists in current directory
dir_path = os.path.dirname(os.path.realpath(__file__))
top_dir_list = os.listdir(dir_path)
saf.find_dir(top_dir_list, "test-folder")
# for item in os.listdir(dir_path):
#     print(item)
#     print(os.path.isfile(item))

# for root, dirs, files in next(os.walk(dir_path))[1]:
#     for dir in dirs:
#         print(dir)


