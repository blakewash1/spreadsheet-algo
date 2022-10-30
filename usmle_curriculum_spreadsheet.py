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

        # 2D dictionary for containing weeks, days, and materials
        course_dict = {}

        for section in sections:
            title = section.find("div", class_="section-title",recursive=False).get_text()
            # print(title)
            # grab list of contents in section
            section_list = section.find("ul", class_="section-list").find_all("li")
            for listing in section_list:
                listing_name = listing.find("span", class_="lecture-name").get_text()
                print(listing_name)

        # for week in weeks:
        #     week_text = (week.find("span", class_="name").get_text())
        #     if desired_week == 0 or int(week_text[-1]) == desired_week:

        #         # variables needed to create an entry to module_dict
        #         sub_dict = {}
        #         day = ""
        #         materials = []

        #         # get each day and its materials
        #         days_and_materials = week.find_all("li")
        #         for item in days_and_materials:
        #             # this could either be a day or course material. If a day, make this the key of the dict
        #             # otherwise, add it to the materials list, which will be the value of the dict
        #             title = item.find("span", {'class':['title', 'locked_title']})["title"]
        #             if title.casefold().startswith("day"):
        #                 # first, add previous day (if any) and its materials to the dict
        #                 if (day):
        #                     sub_dict[day] = materials
        #                 # then start new day w/ new materials
        #                 day = title
        #                 materials = []
        #             else:
        #                 materials.append(title)

        #         # add final day of week to sub_dict
        #         sub_dict[day] = materials
        #         # if there is a desired week chosen by the user, create spreadsheet
        #         if desired_week != 0:
        #             filename = proper_file.replace(".html", "") + " - " + week_text
        #             saf.create_spreadsheet(filename, sub_dict)
        #         # otherwise, add completed sub_dict to module_dict
        #         else:
        #             module_dict[week_text] = sub_dict
        
        # # if no desired week, create spreadsheet for all weeks
        # if desired_week == 0:
        #     filename = proper_file.replace(".html", "") + " - All Weeks"
        #     saf.create_2D_spreadsheet(filename, module_dict)


else:
    print("Webpage not found. Exiting...") 

# add a short delay
time.sleep(2)