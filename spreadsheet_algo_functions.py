import os, os.path as op, xlsxwriter, time
from tqdm import tqdm
import warnings
# for ignoring the progress bar warning (about fractions)
warnings.filterwarnings("ignore")

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

# takes in a dictionary as input and prints its contents to a spreadsheet. Dictionary 
# model should be as follows: { section header : list of contents }
def create_spreadsheet(name, dict):
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

# similar to create_spreadsheet, except takes in a 2D dictionary. Dictionary contents
# should be as follows: { section title : { section header : list of contents } }
def create_2D_spreadsheet(name, dict):
    # creating progress bar
    increment = 100 / len(dict)
    progress_bar = tqdm(total=100, desc="Generating Spreadsheet", 
        colour="green", ncols=150)

    # create spreadsheet using xlsxwriter
    xlsx_path = op.join(os.getcwd(), "find_spreadsheet_here", name +'.xlsx')
    workbook = xlsxwriter.Workbook(xlsx_path)
    worksheet = workbook.add_worksheet()
    title_format = workbook.add_format({'bold': True, 'bg_color': '#B0E0E6', 'font_size': 20})
    title_bg = workbook.add_format({'bg_color': '#B0E0E6'})
    header_format = workbook.add_format({'bold': True, 'bg_color': '#FAFAD2'})
    worksheet.set_row(0, 30)

    # variables for keeping track of column number throughout the spreadsheet
    col = 0
    for title, headers in dict.items():
        # variable for keeping track of row throughout this section
        row = 0
        # widen the length of the first and third column of the section
        worksheet.set_column(col, col, 60)
        worksheet.set_column(col+2, col+2, 30)

        # print section title
        worksheet.write(row, col, title, title_format)
        worksheet.write(row, col+1, "", title_bg)
        worksheet.write(row, col+2, "", title_bg)
        row += 1
        
        for header, content_list in headers.items():
            # writing directory-name, date, and difficulty as section headers
            worksheet.write(row, col, header, header_format)
            worksheet.write(row, col+1, "Date", header_format)
            worksheet.write(row, col+2, "Understanding", header_format)

            # writing contents to the sheet
            for content in content_list:
                row += 1
                worksheet.write(row, col, content)

            # iterating the row number by 2 to create space for the next day
            row += 2
            # updating the progress bar
            time.sleep(0.025)
            progress_bar.update(increment / len(headers))
        
        # iterating the column number by 4 to create space for the next week
        col += 4
           
    progress_bar.close()
    while True:
        try:
            workbook.close()
            break
        except Exception:
            input("Please close the current spreadsheet first. Press Enter you've done so.")

    time.sleep(1)
    print("Spreadsheet created. Saved to 'find_spreadsheet_here' directory.")
    