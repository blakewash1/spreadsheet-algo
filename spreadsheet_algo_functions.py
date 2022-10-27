import os, os.path as op, xlsxwriter, time
from tqdm import tqdm

# for searching for a directory within a list of items. Returns false
# if directory with desired name is not found
def find_dir(dir, name):
    for item in dir:
        if not os.path.isfile(item) and item.casefold() == name.casefold():
            return True
    return False

# takes in a dictionary where key = header name (folder name, week #, etc), and
# value = the list of contents. Iterates through the dictionary and prints to
# a new spreadsheet
def create_spreadsheet(name, dict):
    # creating progress bar
    increment = 100 / len(dict)
    progress_bar = tqdm(total=100, desc="Generating Spreadsheet")
    # for i in tqdm(range(10), desc="Generating Spreadsheet"):
    #     time.sleep(.1)

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
            # progressing the progress bar
            time.sleep(0.025)
            progress_bar.update(increment / len(content_list))

        # iterating the row number by 2 to create space for the next section
        row += 2
           
    progress_bar.close()
    time.sleep(0.5)
    print("Spreadsheet created.")
    workbook.close()

# for writing the contents of a directory to a spreadsheet (in alpha-numeric order)
def create_spreadsheet_old(name, dir_path, dir_list):
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
    for dir in dir_list:
        # writing directory-name, date, and difficulty as section headers
        worksheet.write(row, 0, dir, cell_format)
        worksheet.write(row, 1, "Date", cell_format)
        worksheet.write(row, 2, "Understanding", cell_format)

        # getting the directories contents, then writing them to the sheet
        contents = os.listdir(op.join(dir_path, dir))
        contents.sort()
        for content in contents:
            row += 1
            worksheet.write(row, 0, content)
        # iterating the row number by 2 to create space for the next section
        row += 2
           
    workbook.close()