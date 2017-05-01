# Hacktrickconf 2017 - EmreOvunc
# Python For Hackers

from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://goo.gl/forms/oiiUQckJGJCe6ygA3')
browser.find_element_by_name('entry.712063927').send_keys("Emre Ovunc")
browser.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/input").send_keys("info@emreovunc.com")
browser.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[3]/div[1]/div/div/content/span").click()
time.sleep(2)
browser.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[2]/div[3]/div[2]/div/content/div/label[4]/div/div[1]/div[3]/div").click()
browser.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[2]/div[4]/div[2]/div/content/div/label[1]/div/div[1]/div[3]/div").click()
browser.find_element_by_xpath(".//*[@id='mG61Hd']/div/div[2]/div[3]/div[1]/div/div[2]/content/span").click()
