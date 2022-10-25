## Purpose

The purpose of this script is to take in a folder as input, list out each sub-folder title as columns, then list out the 
titles of each folders' contents as rows beneath aforementioned columns. All of this should be displayed on a spreadsheet,
which is to be automatically downloaded at the end of the writing proccess.
The following is a visual of how the spreadsheet should look:

  FOLDER_1  | DATE | DIFFICULTY |  FOLDER_2  | DATE | DIFFICULTY | ...
 --------------------------------------------------------------------
  CONTENT_1 |      |            | CONTENT_1  |      |            |
  CONTENT_2 |      |            | CONTENT_2  |      |            |
     ...    |      |            |    ...     |      |            |
 
## Requirements
* python version 3.6
* pip install xlsxwriter
* user's folder should exist inside of the "put_folder_here" directory