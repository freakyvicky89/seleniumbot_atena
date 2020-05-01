import sys
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

sleep(10)

driver.close()