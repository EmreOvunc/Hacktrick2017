# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.yahoo.com/')
browser.find_element_by_id("uh-search-box").send_keys("hacktrickconf")
browser.find_element_by_id("uh-search-button").click()
