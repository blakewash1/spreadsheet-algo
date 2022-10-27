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

        # get each week
        top_div = soup.find("div", { "id" : "context_modules" })
        weeks = top_div.find_all('div', recursive=False)
        total_weeks = len(weeks)
       
        # variable for the user-chosen week. If 0, do all weeks
        desired_week = 0
        # check if user wants all weeks or a single week
        while True:
            print("Create a spreadsheet for 1) a single week or 2) all weeks?")
            try:
                answer = int(input('Enter 1 or 2: '))
            except ValueError:
                answer = 0

            if answer != 1 and answer != 2:
                print('Please enter a valid choice.')
                time.sleep(1)
                continue
            elif answer == 1:
                time.sleep(0.5)
                while True:
                    try:
                        week_answer = int(input('Which week? (Enter as a #): '))
                    except ValueError:
                        week_answer = 0

                    if (week_answer > total_weeks or week_answer < 1):
                        print('Please enter a valid week #.')
                        time.sleep(1)
                        continue
                    else:
                        desired_week = week_answer
                        break
                break
            else:
                break

        # 2D dictionary for containing weeks, days, and materials
        module_dict = {}

        for week in weeks:
            week_text = (week.find("span", class_="name").get_text())
            if desired_week == 0 or int(week_text[-1]) == desired_week:

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
                            for key, values in sub_dict.items():
                                print(key)
                                print(values)
                        # then start new day w/ new materials
                        day = title
                        materials = []
                    else:
                        materials.append(title)

                # add final day of week to sub_dict
                sub_dict[day] = materials
                # if there is a desired week chosen by the user, create spreadsheet
                if desired_week != 0:
                    filename = proper_file.replace(".html", "") + "-" + week_text
                    print(filename)
                    saf.create_spreadsheet(filename, sub_dict)
                # otherwise, add completed sub_dict to module_dict
                else:
                    module_dict[week_text] = sub_dict





else:
    print("Webpage not found. Exiting...") 

# add a short delay
time.sleep(2)