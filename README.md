# Folder_Spreadsheet
## Purpose

The purpose of this script is to take in a folder as input, list out each sub-folder title as columns, then list out the 
titles of each folders' contents as rows beneath aforementioned columns. All of this should be displayed on a spreadsheet,
which is to be automatically downloaded at the end of the writing proccess.
The following is a visual of how the spreadsheet should look:

   FOLDER_1   | DATE | UNDERSTANDING   
 ---------------------------------
  CONTENT_1 |      |             
  CONTENT_2 |      |            
     ...    |      |             
   FOLDER_2   | DATE | UNDERSTANDING 
 ---------------------------------
  CONTENT_1 |      |             
  CONTENT_2 |      |            
     ...    |      |             
 
## Requirements
* python version 3.6
* pip install xlsxwriter
* pip install tqdm
* user's folder should exist inside of the "put_folder_here" directory

# AUC_Module_Spreadsheet
## Purpose

The purpose of this script is to take in a webpage source (html) as input, list out each Week title as headers, then list out the 
week's contents as rows beneath aforementioned headers. All of this should be displayed on a spreadsheet,
which is to be automatically downloaded at the end of the writing proccess.
The following is a visual of how the spreadsheet should look:

   WEEK_1   | DATE | UNDERSTANDING   
 ---------------------------------
  CONTENT_1 |      |             
  CONTENT_2 |      |            
     ...    |      |             
   WEEK_2   | DATE | UNDERSTANDING 
 ---------------------------------
  CONTENT_1 |      |             
  CONTENT_2 |      |            
     ...    |      |             

## Requirements
* python version 3.6
* pip install xlsxwriter
* pip install tqdm
* this code only works with AUC courses webpage https://auc.instructure.com/courses/1380/modules