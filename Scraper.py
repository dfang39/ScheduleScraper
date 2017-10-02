from lxml import html
import requests
import os
import openpyxl
from datetime import datetime

page = requests.get('http://ottershockey.com/schedule/60/8')
tree = html.fromstring(page.content)


dates = tree.xpath("//table")
# opponents = tree.xpath('//td[@class="opponent-td"]/text()')
# locations = tree.xpath('//td[@class="sch-col-3"]/text()')
# times = tree.xpath('//td[@class="time-td"]/text()')

# times = tree.xpath('//td[@class="time-td"]/text()')

print(tree.find_class("stats-data-table"))

print(len(dates))
for date in dates:
    print(date.xpath("@data-raw-date"))

#print(datetime.strptime(dates[1], '%b %d'))
# print(opponents)
#print(locations)
# print(times)

# print(dates.index("Jan 2"))
# game_dates = []
# for i in range(0, 37):
    # game_dates.append(dates[i] + " 2017 " + times[i])
# for i in range(38, len(dates)):
    # game_dates.append(dates[i] + " 2018 " + times[i])



# for i in range(0, len(game_dates)):
    # game_dates[i] = datetime.strptime(game_dates[i], '%b %d %Y %I:%M %p')

# print(game_dates)

out_folder = "C:\\Users\\DanFang\\Desktop"
os.chdir(out_folder)


# out_workbook = openpyxl.Workbook()
# sheet = out_workbook.active

# row_count = 1
# for i in range(1, len(game_dates)):
    # if "@" not in opponents[i]:
        # sheet['A' + str(row_count)] = game_dates[i]
        # sheet['B' + str(row_count)] = "New Jersey Devils " + opponents[i]
        # row_count += 1

# out_workbook.save("Devils.xlsx")