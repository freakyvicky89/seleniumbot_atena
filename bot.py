import sys
from random import randrange
from time import sleep
from selenium import webdriver

if len(sys.argv) > 1 and sys.argv[1]:
    development = True
else:
    development = False

driver_options = webdriver.ChromeOptions()

if not development:
    driver_options.add_argument('headless')

driver = webdriver.Chrome(options=driver_options)
driver.get('https://www.wp.pl/')
sleep(2)
driver.find_element_by_xpath('//button[contains(.,"AKCEPTUJ")]').click()
sleep(2)
news_links = driver.find_elements_by_xpath('//div[@data-st-area="Wiadomosci"]//a')
news_links[randrange(0, len(news_links))].click()



#driver.close()