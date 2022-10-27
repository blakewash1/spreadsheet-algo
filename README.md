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
* python version 3.7
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
* python version 3.7
* pip install xlsxwriter
* pip install tqdm
* this code only works with AUC courses webpage https://auc.instructure.com/courses/1380/modules

## Instructions
1) Go to AUC Instructure website, go to Modules 
2) Right-click and click "Save as..." 
3) Save webpage source (html) in the folder called "put_html_here" under a new, shorter name
4) in File Explorer, go to the "spreadsheet-algo" folder 
5) Click on address bar, type in "powershell," press Enter
6) Type in "python auc_module_spreadsheet.py" Press Enter
7) When prompted for the name of the webpage source, enter the name of the html you saved in step 3 (make sure you put the file type ".html" at the end)
8) If code is successful, you can find the new spreadsheet in the "find_spreadsheet_here" folder