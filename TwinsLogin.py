from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from lxml import html
import os
import openpyxl
from datetime import datetime

browser = webdriver.Chrome('C:\\Users\\DanFang\\Documents\\chromedriver.exe')
browser.implicitly_wait(3)
url = 'https://mytickets.tickets.com/buy/MyTicketsServlet?agency=TWNM_MYTIXX&orgid=30368&supplier_code=TWNM&user_context=S_tomcat_irprwebmyt3_1489700445369_36288|S|tomcat_irprwebmyt1|purchase.tickets.com|en|US|null|TWNM_DONATE&trxstate=315&mlbamsp=true'
browser.get(url)


# browser.find_element_by_id('nextPage').click();
# browser.find_element_by_id('nextPage').click();
# browser.find_element_by_id('nextPage').click();
# select = Select(browser.find_element_by_class_name('filter-group__dropdown-select'))

# select.select_by_visible_text('2017-18 Regular Season')

username = browser.find_element_by_id("mytkts_user_name")
password = browser.find_element_by_id("mytkts_password")

username.send_keys("1065356")
password.send_keys("tix4tots")

browser.find_element_by_link_text("Log In").click()

WebDriverWait(browser, 30).until(
    expected_conditions.presence_of_element_located((By.ID, "todo_pending_transfers"))
)

browser.find_element_by_id("todo_pending_transfers").click()

innerHTML = browser.execute_script("return document.body.innerHTML")
print(innerHTML)