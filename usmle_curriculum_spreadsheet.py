import os, os.path as op, spreadsheet_algo_functions as saf, time
from re import sub
from tqdm import tqdm
from bs4 import BeautifulSoup as bs

# get name of webpage source from user input
user_file = input("Enter name of webpage source (html): ")

# check if user html exists in the "put html_here" directory. 
# If not, exit program
dir_path = op.join(os.getcwd(), "put_html_here")
proper_file = saf.find_file(dir_path, user_file)

if proper_file != "nope":
    print("Webpage found.")
    time.sleep(1)

    with open(op.join(dir_path, proper_file)) as file:
        soup = bs(file, "html.parser")

        # grab each course section
        sections = soup.find_all('div', {'class':['col-sm-12', 'course-section']})

        # dictionary for containing header titles and content lists
        course_dict = {}

        for section in sections:
            section_title = section.find("div", class_="section-title",recursive=False).get_text()
            # trim title down to only the name
            section_title = section_title.split('\n')[6].strip()
            # variable for keeping track of contents in this section
            section_list_names = []
            # grab list of contents in section
            section_list = section.find("ul", class_="section-list").find_all("li")
            for listing in section_list:
                listing_name = listing.find("span", class_="lecture-name").get_text()
                # trim listing down to only the name
                listing_name = listing_name.split('\n')[1].strip()
                section_list_names.append(listing_name)

            course_dict[section_title] = section_list_names
        
        # create spreadsheet
        filename = proper_file.replace(".html", "")
        saf.create_spreadsheet(filename, course_dict)

else:
    print("Webpage not found. Exiting...") 

# add a short delay
time.sleep(2)