from selenium import webdriver
from selenium.webdriver.support.ui import Select
from lxml import html
import os
import openpyxl
from datetime import datetime
import time

browser = webdriver.Chrome('C:\\Users\\DanFang\\Documents\\chromedriver.exe')
browser.implicitly_wait(3)


url = 'https://pittsburghpanthers.com/schedule.aspx?path=wbball'
browser.get(url)

SCROLL_PAUSE_TIME = 0.8

"""
# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
"""
# browser.find_element_by_id('nextPage').click();
# browser.find_element_by_id('nextPage').click();
# browser.find_element_by_id('nextPage').click();
#select = Select(browser.find_element_by_id('ctl00_cplhMainContent_ddl_location'))
#select.select_by_value("home")
# select.select_by_visible_text('Home Game')

#browser.implicitly_wait(5)
#time.sleep(5)

innerHTML = browser.execute_script("return document.body.innerHTML")
print(innerHTML)


tree = html.fromstring(innerHTML)
days = tree.xpath("//div[@class='sidearm-schedule-game-opponent-date flex-item-1']/span[position()=1]/text()")
# days = tree.xpath("//tbody[@class='date-tbody home-game future-game']/tr/td/div/div[@class='date-label']/text()")
times = tree.xpath("//div[@class='sidearm-schedule-game-opponent-date flex-item-1']/span[position()=2]/text()")
away_teams = tree.xpath("//div[@class='sidearm-schedule-game-opponent-text']/span[position()=2]/a/text()")
# home_teams = tree.xpath("//ul[contains(@class, 'game-teams')]/li[position()=2]/text()")
venues = tree.xpath("//div[@class='sidearm-schedule-game-location']/span[position()=1]/text()")
# is_away = tree.xpath("//div[@class='sidearm-schedule-game-opponent-text']/span[position()=1]/text()")
# dates = list(filter(lambda x: x != '\n', orig_dates))

print(days)

# print(days, len(days))
print(times, len(times))
print(away_teams, len(away_teams))
print(venues)
# print(is_away, len(is_away))
# print(away_teams)
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

# print(datetime.strptime(days[0] + " 2018 " + times[0].replace(" ET", ""), '%a, %b %d %Y %I:%M %p'))
# print(opponents)
# print(locations)
# print(times)

# print(dates.index("2018-01-03"))
# print(dates.index("Jan. 3"))

"""
game_dates = []

year_break = "Jan 3 (Thu)"
for i in range(0, days.index(year_break)):
    game_dates.append(datetime.strptime(days[i] + " 2018 " + times[i].replace("TBA", "8 AM").replace("A.M.", "AM").replace("P.M.", "PM").replace(" ET", ""), '%b %d (%a) %Y %I %p'))
for i in range(days.index(year_break), len(days)):
    game_dates.append(datetime.strptime(days[i] + " 2019 " + times[i].replace("TBA", "8 AM").replace("A.M.", "AM").replace("P.M.", "PM").replace(" ET", "").replace("Mar 10 (Sun)", "8 AM"), '%b %d (%a) %Y %I %p'))

print(game_dates)
# real_dates = []
#for i in range(dates.index('Nov 4 (Sat)'), 6):
    #real_dates.append(datetime.strptime(dates[i] + " 2017 " + times[i], '%b %d (%a) %Y %I:%M %p '))
# for i in range(0, len(days)):
    # try:
        # real_dates.append(datetime.strptime(days[i], '%m/%d/%Y %I:%M %p '))
    # except:
        # real_dates.append(datetime.strptime(dates[i] + "0" + times[i].replace(" CT", ""), '%A, %B %d, %Y %I:%M%p'))

#for i in range(dates.index('Jan 2 (Tue)'), len(dates) -1):  + times[i].replace(" CT", "")
    #real_dates.append(datetime.strptime(dates[i] + " 2018 " + times[i], '%b %d (%a) %Y %I:%M %p '))

# print(real_dates)

# print(len(real_dates))
# print(len(venues))
# print(len(away_teams))

out_folder = "C:\\Users\\DanFang\\Desktop\\EventSeasons"
os.chdir(out_folder)


out_workbook = openpyxl.Workbook()
sheet = out_workbook.active

row_count = 1
for i in range(0, len(away_teams)):
    #Wsheet['A' + str(row_count)] = game_dates[i]
    sheet['B' + str(row_count)] = "Pitt Panthers Women's Basketball vs. " + away_teams[i]
    #.title().replace("\n", "").replace("\t", "").strip()
    #sheet['C' + str(row_count)] = times[i]
    row_count += 1

out_workbook.save("pittwbb2018opps.xlsx")

browser.quit()