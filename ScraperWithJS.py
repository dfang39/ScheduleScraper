from selenium import webdriver
from selenium.webdriver.support.ui import Select
from lxml import html
import os
import openpyxl
from datetime import datetime

browser = webdriver.Chrome('C:\\Users\\DanFang\\Documents\\chromedriver.exe')
browser.implicitly_wait(3)
url = 'https://sp1.glitnirticketing.com/spticket/mobile/evlistm.php?_ga=2.205061840.1371212482.1525438833-331170799.1524228821&refresh=1525439109'
browser.get(url)


# browser.find_element_by_id('nextPage').click();
# browser.find_element_by_id('nextPage').click();
# browser.find_element_by_id('nextPage').click();
# select = Select(browser.find_element_by_class_name('filter-group__dropdown-select'))

# select.select_by_visible_text('2017-18 Regular Season')

innerHTML = browser.execute_script("return document.body.innerHTML")
print(innerHTML)


tree = html.fromstring(innerHTML)
# orig_dates = tree.xpath("//div[@class='month-date']/text()")
days = tree.xpath("//td[@class='eventdate']/span/text()")

# times = tree.xpath("//span[@class='match_time']/text()")
away_teams = tree.xpath("//td[@class='eventdetails']/text()")
# home_teams = tree.xpath("//ul[contains(@class, 'game-teams')]/li[position()=2]/text()")
# venues = tree.xpath("//div[@class='match_info match_location_short']/text()")

# dates = list(filter(lambda x: x != '\n', orig_dates))

# print(orig_dates)

print(days)

print(away_teams)
"""
# print(home_teams)
print(times)
print(venues)
"""
# str_away_teams = list(filter(lambda x: x != "", map(lambda x: str(x).replace("\n", "").strip().title(), away_teams)))
# str_home_teams = list(filter(lambda x: x != "", map(lambda x: str(x).replace("\n", "").strip().title(), home_teams)))
# print(str_away_teams)
# print(str_home_teams)
#str_home_teams = list(filter(lambda x: x != "", map(lambda x: str(x).replace("\n", "").strip().title(), home_teams)))
"""

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

"""
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
"""
print(len(real_dates))
print(len(venues))
print(len(away_teams))
"""
out_folder = "C:\\Users\\DanFang\\Desktop\\EventSeasons"
os.chdir(out_folder)


out_workbook = openpyxl.Workbook()
sheet = out_workbook.active

row_count = 1
for i in range(0, len(real_dates)):
    sheet['A' + str(row_count)] = real_dates[i]
    sheet['B' + str(row_count)] = "Minnesota United FC vs. " + away_teams[i].title().replace("\n", "").replace("\t", "").strip()
    # sheet['C' + str(row_count)] = venues[i]
    row_count += 1

out_workbook.save("saints.xlsx")

