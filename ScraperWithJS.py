from selenium import webdriver
from selenium.webdriver.support.ui import Select
from lxml import html
import os
import openpyxl
from datetime import datetime

browser = webdriver.Chrome('C:\\Users\\DanFang\\Downloads\\chromedriver_win32\\chromedriver.exe')
browser.implicitly_wait(3)
url = 'http://www.ticketmaster.com/artist/1373960?tm_link=tm_changeloc_cities'
browser.get(url)

browser.find_element_by_id('nextPage').click();
browser.find_element_by_id('nextPage').click();
browser.find_element_by_id('nextPage').click();
#select = Select(browser.find_element_by_class_name('filter-group__dropdown-select'))

#select.select_by_visible_text('2017-18 Regular Season')

innerHTML = browser.execute_script("return document.body.innerHTML")
print(innerHTML)

tree = html.fromstring(innerHTML)
dates = tree.xpath("//div[@class='month']/abbr/text()")
days = tree.xpath("//div[@class='date']/text()")
times = tree.xpath("//div[@class='padH10']/text()")
away_teams = tree.xpath("//span[@class='eventName']/text()")
#home_teams = tree.xpath("//ul[contains(@class, 'game-teams')]/li[position()=2]/text()")
venues = tree.xpath("//a[@class='event']/text()")

print(dates)
print(days)
print(away_teams)
#print(home_teams)
print(times)
print(venues)

# str_away_teams = away_teams[::2]
# str_home_teams = away_teams[1::2]
# print(str_away_teams)
# print(str_home_teams)
#str_home_teams = list(filter(lambda x: x != "", map(lambda x: str(x).replace("\n", "").strip().title(), home_teams)))


str_times = times[1::2]
print(str_times)

# print(datetime.strptime(dates[1], '%b %d (%a)'))
# print(opponents)
# print(locations)
# print(times)

# print(dates.index("2018-01-03"))
# print(dates.index("Jan. 3"))
game_dates = []
# for i in range(0, dates.index("2018-01-03")):
    # game_dates.append(dates[i] + " 2017 " + str(times[i]).replace(" ET", ""))
# for i in range(dates.index("2018-01-03")):
    # game_dates.append(dates[i] + " 2018 " + str(times[i]).replace(" ET", ""))


for i in range(0, len(dates)):
    game_dates.append(datetime.strptime(dates[i] + " " + days[i] + " 2018 " + str_times[i], '%b %d %Y %I:%M %p'))

print(game_dates)

out_folder = "C:\\Users\\DanFang\\Desktop"
os.chdir(out_folder)


out_workbook = openpyxl.Workbook()
sheet = out_workbook.active

row_count = 1
for i in range(0, len(game_dates)):
    if "Covelli Centre" in venues[i]:
        sheet['A' + str(row_count)] = game_dates[i]
        sheet['B' + str(row_count)] = away_teams[i]
        # sheet['C' + str(row_count)] = venues[i]
        row_count += 1

out_workbook.save("YoungstownPhantoms4.xlsx")
