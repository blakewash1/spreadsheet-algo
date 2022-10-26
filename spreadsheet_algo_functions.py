import os, os.path as op, xlsxwriter

# for searching for a directory within a list of items. Returns false
# if directory with desired name is not found
def find_dir(dir, name):
    for item in dir:
        if not os.path.isfile(item) and item.casefold() == name.casefold():
            return True
    return False

# for writing the contents of a directory to a spreadsheet (in alpha-numeric order)
def create_spreadsheet(name, dir_path, dir_list):
    # create spreadsheet using xlsxwriter
    xlsx_path = op.join(os.getcwd(), "find_spreadsheet_here", name +'.xlsx')
    workbook = xlsxwriter.Workbook(xlsx_path)
    worksheet = workbook.add_worksheet()
    cell_format = workbook.add_format({'bold': True, 'bg_color': '#FAFAD2'})

    # widen the length of the first column
    worksheet.set_column(0, 0, 50)
    
    # variable for keeping track of row num as we go down the spreadsheet
    row = 0
    for dir in dir_list:
        # writing directory-name, date, and difficulty as section headers
        worksheet.write(row, 0, dir, cell_format)
        worksheet.write(row, 1, "Date", cell_format)
        worksheet.write(row, 2, "Difficulty", cell_format)

        # getting the directories contents, then writing them to the sheet
        contents = os.listdir(op.join(dir_path, dir))
        contents.sort()
        for content in contents:
            row += 1
            worksheet.write(row, 0, content)
        # iterating the row number by 2 to create space for the next section
        row += 2
           
    workbook.close()