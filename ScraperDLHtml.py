from selenium import webdriver
from selenium.webdriver.support.ui import Select
from lxml import html
import os
import openpyxl
from datetime import datetime
import urllib3

htmlFile = open("Vikings.html", "r", encoding='utf-8')
htmlString = htmlFile.read()



tree = html.fromstring(htmlString)
# orig_dates = tree.xpath("//div[@class='month-date']/text()")
init_info = tree.xpath("//div[@class='col-xs-4']/div/strong/text()")
row = tree.xpath("//div[@class='col-xs-4']/strong/div/strong/text()")

section = []
seat = []

for i in range(0, len(init_info)):
    if i % 2 == 0:
        section.append(init_info[i])
    else:
        seat.append(init_info[i])

print(len(section))
print(len(row))
print(len(seat))

seats_together = [None] * 132
group_count = 0
for i in range(0, len(section)):
    if i != 0:
        print(section[i-1] == section[i], row[i-1] == row[i], int(seat[i-1]), int(seat[i]))

    if i == 0:
        seats_together[group_count] = []
        seats_together[group_count].append("Section " + section[i] + " Row " + row[i] + " Seat " + seat[i] + "\n")
    elif section[i-1] == section[i] and row[i-1] == row[i] and int(seat[i]) - int(seat[i-1]) == 1:
        seats_together[group_count].append("Section " + section[i] + " Row " + row[i] + " Seat " + seat[i] + "\n")
    else:
        group_count += 1;
        seats_together[group_count] = []
        seats_together[group_count].append("Section " + section[i] + " Row " + row[i] + " Seat " + seat[i] + "\n")

seats_together_clean = [x for x in seats_together if x != None]
print(seats_together_clean)
# times = tree.xpath("//span[@class='match_time']/text()")
#away_teams = tree.xpath("//td[@class='eventdetails']/text()")
# home_teams = tree.xpath("//ul[contains(@class, 'game-teams')]/li[position()=2]/text()")
# venues = tree.xpath("//div[@class='match_info match_location_short']/text()")

# dates = list(filter(lambda x: x != '\n', orig_dates))

# print(orig_dates)

"""
#print(away_teams)

# print(home_teams)
print(times)
print(venues)

# str_away_teams = list(filter(lambda x: x != "", map(lambda x: str(x).replace("\n", "").strip().title(), away_teams)))
# str_home_teams = list(filter(lambda x: x != "", map(lambda x: str(x).replace("\n", "").strip().title(), home_teams)))
# print(str_away_teams)
# print(str_home_teams)
#str_home_teams = list(filter(lambda x: x != "", map(lambda x: str(x).replace("\n", "").strip().title(), home_teams)))


# str_times = times[1::2]
# print(str_times)

# print(datetime.strptime(dates[1], '%b %d (%a)'))
# print(opponents)
# print(locations)
# print(times)

# print(dates.index("2018-01-03"))
# print(dates.index("Jan. 3"))
# game_dates = []
# for i in range(0, dates.index("Jan. 5")):
    # game_dates.append(dates[i] + " 2017 " + str(times[i]).replace(" EDT", "").replace(" EST", ""))
# for i in range(dates.index("Jan. 5"), len(dates)):
    # game_dates.append(dates[i] + " 2018 " + str(times[i]).replace(" EDT", "").replace(" EST", ""))


real_dates = []
#for i in range(dates.index('Nov 4 (Sat)'), 6):
    #real_dates.append(datetime.strptime(dates[i] + " 2017 " + times[i], '%b %d (%a) %Y %I:%M %p '))
for i in range(0, len(days)):
    # try:
        real_dates.append(datetime.strptime(days[i], '%m/%d/%Y %I:%M %p '))
    # except:
        # real_dates.append(datetime.strptime(dates[i] + "0" + times[i].replace(" CT", ""), '%A, %B %d, %Y %I:%M%p'))

#for i in range(dates.index('Jan 2 (Tue)'), len(dates) -1):  + times[i].replace(" CT", "")
    #real_dates.append(datetime.strptime(dates[i] + " 2018 " + times[i], '%b %d (%a) %Y %I:%M %p '))

print(real_dates)

print(len(real_dates))
print(len(venues))
print(len(away_teams))
"""
out_folder = "C:\\Users\\DanFang\\Desktop"
os.chdir(out_folder)


out_workbook = openpyxl.Workbook()
sheet = out_workbook.active

row_count = 1
for i in range(0, len(seats_together_clean)):
    sheet['A' + str(row_count)] = len(seats_together_clean[i])
    sheet['B' + str(row_count)] = "".join(seats_together_clean[i])
    # sheet['C' + str(row_count)] = venues[i]
    row_count += 1

out_workbook.save("vikings2-7.xlsx")

