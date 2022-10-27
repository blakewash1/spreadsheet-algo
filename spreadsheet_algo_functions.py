import os, os.path as op, xlsxwriter, time
from tqdm import tqdm

# for searching for a directory within a list of items. Returns True
# if directory with desired name is found, False if otherwise
def find_dir(dir_path, name):
    # get list of items in directory
    dir_list = os.listdir(dir_path)
    # converts chars to lowercase and removes any spaces from name
    name = name.casefold().replace(" ", "")

    for item in dir_list:
        if (not os.path.isfile(op.join(dir_path, item)) and 
            item.casefold().replace(" ", "") == name):
            
            return True
    
    return False

# for searching for a file within a list of items. Returns the proper name
# of the file if it is found, otherwise returns "nope"
def find_file(dir_path, name):
    # get list of items in directory
    dir_list = os.listdir(dir_path)
    # converts chars to lowercase and removes any spaces from name
    name = name.casefold().replace(" ", "")

    for item in dir_list:
        if (os.path.isfile(op.join(dir_path, item)) and 
            item.casefold().replace(" ", "") == name):
            
            return item
    
    return "nope"

# takes in a dictionary where key = header name (folder name, day #, etc), and
# value = the list of contents. Iterates through the dictionary and prints to
# a new spreadsheet
# also takes in an optional argument "titles" which can be a list of section titles
# If this is populated, each title will appear in larger, bold font at the top of each 
# corresponding section
def create_spreadsheet(name, dict, titles=[]):
    # creating progress bar
    increment = 100 / len(dict)
    progress_bar = tqdm(total=100, desc="Generating Spreadsheet", 
        colour="green", ncols=150)

    # create spreadsheet using xlsxwriter
    xlsx_path = op.join(os.getcwd(), "find_spreadsheet_here", name +'.xlsx')
    workbook = xlsxwriter.Workbook(xlsx_path)
    worksheet = workbook.add_worksheet()
    cell_format = workbook.add_format({'bold': True, 'bg_color': '#FAFAD2'})

    # widen the length of the first and third column
    worksheet.set_column(0, 0, 60)
    worksheet.set_column(2, 2, 30)

    # variable for keeping track of row num as we go down the spreadsheet
    row = 0
    for header, content_list in dict.items():
        # writing directory-name, date, and difficulty as section headers
        worksheet.write(row, 0, header, cell_format)
        worksheet.write(row, 1, "Date", cell_format)
        worksheet.write(row, 2, "Understanding", cell_format)

        # writing contents to the sheet
        for content in content_list:
            row += 1
            worksheet.write(row, 0, content)
            # updating the progress bar
            time.sleep(0.025)
            progress_bar.update(increment / len(content_list))

        # iterating the row number by 2 to create space for the next section
        row += 2
           
    progress_bar.close()
    print("Spreadsheet created. Saved to 'find_spreadsheet_here' directory.")
    workbook.close()