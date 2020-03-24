import csv
from datetime import datetime, date

today = datetime.today()

badges_dict = {
    "blog": {"csv_row": 1, "streak": 0},
    "meditation": {"csv_row": 2, "streak": 0},
    "yoga": {"csv_row": 3, "streak": 0},
    "failio": {"csv_row": 4, "streak": 0},
    "sleep": {"csv_row": 5, "streak": 0},
    "call": {"csv_row": 6, "streak": 0}
}

with open('/home/ted/Desktop/data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

for cat in data[0][1:]:
    badges_dict[cat]["streak"] = 1


for row in data[1:]: # loop through dates
    datetime_obj = datetime.strptime(row[0], '%Y-%m-%d') # convert string to datetime obj
    if datetime_obj <= today: # if today or before
        for i, col in enumerate(row): # loop through cells in row
            if i == 0: continue # date
            for key in badges_dict: # loop through badges dict
                if badges_dict[key]["csv_row"] == i: # if col corresponds
                    if int(col) == 0: badges_dict[key]["streak"] = 0
                    else: badges_dict[key]["streak"] += int(col)
