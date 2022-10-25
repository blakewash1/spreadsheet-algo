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
    print(xlsx_path)
    workbook = xlsxwriter.Workbook(xlsx_path)
    worksheet = workbook.add_worksheet()
    cell_format = workbook.add_format()
    cell_format.set_bold()

    # variable to keep track of the column number on the spreadsheet
    col = 0
    for dir in dir_list:
        # writing 
        row = 0
        # writing directory-name, date, and difficulty as section headers
        worksheet.write(row, col, dir, cell_format)
        worksheet.write(row, col + 1, "Date", cell_format)
        worksheet.write(row, col + 2, "Difficulty", cell_format)
        # getting the directories contents, then writing them
        contents = os.listdir(op.join(dir_path, dir))
        contents.sort()
        for content in contents:
            row += 1
            worksheet.write(row, col, content)

        # iterating the column number by 3 to start the section for the next sub-directory
        col += 3
           
    workbook.close()