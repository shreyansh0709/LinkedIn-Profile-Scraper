import parameters
from time import sleep
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:\Users\Lenovo\Desktop\chromedriver')

driver.get('https://www.google.com')
sleep(3)

search_query = driver.find_element_by_name('q')

search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "London"')

search_query.send_keys(Keys.RETURN)

linkedin_urls = driver.find_elements_by_class_name('iUh30')

linkedin_urls = [url.text for url in linkedin_urls]

linkedin_urls
