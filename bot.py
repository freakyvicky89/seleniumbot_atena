import credentials
import sys
from datetime import datetime
from pymongo import MongoClient
from random import choice, randrange
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if len(sys.argv) > 1 and sys.argv[1]:
    development = True
else:
    development = False

if not development:
    sleep(randrange(0, 1800))

db_client = MongoClient(credentials.cluster_string)


db = db_client.get_database('cytaty')
dao = db['autorzy']
random_author = dao.find().limit(-1).skip(randrange(dao.count({}))).next()

driver_options = webdriver.ChromeOptions()

if not development:
    driver_options.add_argument('headless')

driver = webdriver.Chrome(options=driver_options)

driver.get('https://www.wp.pl/')
sleep(2)
driver.find_element_by_xpath('//button[contains(.,"AKCEPTUJ")]').click()
sleep(2)
news_links = driver.find_elements_by_xpath('//div[@data-st-area="Wiadomosci"]//a')
news_links[0].location_once_scrolled_into_view
sleep(1)
choice(news_links).click()
sleep(1)
driver.switch_to.window(driver.window_handles[0])
sleep(1)

comment_section = driver.find_elements_by_xpath('//div[contains(.,"Podziel się opinią")]')[-1]
comment_section.location_once_scrolled_into_view
sleep(5)
comment_section.location_once_scrolled_into_view
driver.find_elements_by_xpath('//div[contains(.,"#StopMowie")]')[-1].click()
sleep(2)
comment_section.location_once_scrolled_into_view
sleep(1)

driver.switch_to.active_element.send_keys(choice(random_author['cytaty']))
sleep(1)
driver.switch_to.active_element.send_keys(Keys.TAB)
sleep(1)
driver.switch_to.active_element.send_keys(random_author['nazwa'])
sleep(1)
driver.switch_to.active_element.send_keys(Keys.ENTER)

sleep(10)
driver.save_screenshot(str(datetime.timestamp(datetime.now())) + ".png")
driver.close()
