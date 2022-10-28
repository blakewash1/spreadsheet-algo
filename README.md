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
The purpose of this script is to take in a webpage source (html) as input, list out each Week title, each day, then list out the 
day's contents as rows beneath aforementioned days. All of this should be displayed on a spreadsheet,
which is to be automatically downloaded at the end of the writing proccess.
The following is a visual of how the spreadsheet should look:

  WEEK_1                             WEEK_2 
 -------------------------------------------------------------------
   DAY_1   | DATE | UNDERSTANDING     DAY_1   | DATE | UNDERSTANDING
 -------------------------------------------------------------------
  CONTENT_1 |      |                CONTENT_1 |      |                
  CONTENT_2 |      |                CONTENT_2 |      |            
     ...    |      |                   ...    |      |              
   DAY_2   | DATE | UNDERSTANDING     DAY_2   | DATE | UNDERSTANDING
 --------------------------------------------------------------------
  CONTENT_1 |      |                CONTENT_1 |      |            
  CONTENT_2 |      |                CONTENT_2 |      |            
     ...    |      |                   ...    |      |       
 

## Requirements
* python version 3.7
* pip3 install xlsxwriter
* pip3 install tqdm
* pip3 install beautifulsoup4
* this code only works with AUC courses webpage https://auc.instructure.com/courses/1380/modules

## Instructions
1) Go to AUC Instructure website, go to Modules 
2) Right-click on the page and click "Save as..." 
3) Save webpage source (html) in the folder called "put_html_here" under a new, shorter name
4) in File Explorer, go to the "spreadsheet-algo" folder 
5) Click on address bar, type in "powershell," press Enter
6) Type in "python auc_module_spreadsheet.py" Press Enter
7) When prompted for the name of the webpage source, enter the name of the html you saved in step 3 (make sure you put the file type ".html" at the end)
8) Follow the prompts to choose whether you'd like a single week's worth of content or all weeks
9) If code is successful, you can find the new spreadsheet in the "find_spreadsheet_here" folder


# USMLE_Curriculum_Spreadsheet

## Purpose
The purpose of this script is similar to the auc_module_spreadsheet, to take in a webpage source (html) and list out the page's contents on a
spreadsheet. Except this time, the spreadsheet will look more like the folder_spreadsheet, since there is just a list of headers and their materials.
The following is a visual of how the spreadsheet should look:

   HEADER_1 | DATE | UNDERSTANDING   
 ---------------------------------
  CONTENT_1 |      |             
  CONTENT_2 |      |            
     ...    |      |             
   HEADER_2 | DATE | UNDERSTANDING 
 ---------------------------------
  CONTENT_1 |      |             
  CONTENT_2 |      |            
     ...    |      |             

## Requirements
* python version 3.7
* pip3 install xlsxwriter
* pip3 install tqdm
* pip3 install beautifulsoup4
* this code only works with USMLE Course Curriculum webpage https://hyguru.teachable.com/courses/enrolled/1602338

## Instructions
1) Go to USMLE Course website, go to Course Curriculum 
2) Right-click on the page and click "Save as..." 
3) Save webpage source (html) in the folder called "put_html_here" under a new, shorter name
4) in File Explorer, go to the "spreadsheet-algo" folder 
5) Click on address bar, type in "powershell," press Enter
6) Type in "python usmle_curriculum_spreadsheet.py" Press Enter
7) When prompted for the name of the webpage source, enter the name of the html you saved in step 3 (make sure you put the file type ".html" at the end)
8) If code is successful, you can find the new spreadsheet in the "find_spreadsheet_here" folder