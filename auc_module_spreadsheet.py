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
    time.sleep(1.5)

    with open(op.join(dir_path, proper_file)) as file:
        soup = bs(file, "html.parser")
        # 2D dictionary for containing weeks, days, and materials
        module_dict = {}

        # get each week
        top_div = soup.find("div", { "id" : "context_modules" })
        weeks = top_div.find_all('div', recursive=False)
        for week in weeks:
            week_text = (week.find("span", class_="name").get_text())
            # variables needed to create an entry to module_dict
            sub_dict = {}
            day = ""
            materials = []

            # get each day and its materials
            days_and_materials = week.find_all("li")
            for item in days_and_materials:
                # this could either be a day or course material. If a day, make this the key of the dict
                # otherwise, add it to the materials list, which will be the value of the dict
                title = item.find("span", {'class':['title', 'locked_title']})["title"]
                if title.casefold().startswith("day"):
                    # first, add previous day (if any) and its materials to the dict
                    if (day):
                        sub_dict[day] = materials
                        print(day)
                        print(materials)
                    # then start new day w/ new materials
                    day = title
                    materials.clear()
                else:
                    materials.append(title)

            # add final day of week to sub_dict
            sub_dict[day] = materials
            print(day)
            print(materials)
            # add completed sub_dict to module_dict
            module_dict[week_text] = sub_dict





else:
    print("Webpage not found. Exiting...") 

# add a short delay
time.sleep(2)