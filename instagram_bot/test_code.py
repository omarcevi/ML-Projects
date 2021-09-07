import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secret_info import mygtlist
from comment_list import comments_list_noemo
import random
import time


username_1 = mygtlist[0]
password_1 = mygtlist[1]

browser = webdriver.Chrome('./chromedriver.exe')
print('Opened browser')
print('Waiting')
time.sleep(3)

browser.get('https://www.instagram.com/')
print('Opened browser')
print('Waiting')
time.sleep(3)

#input username
username_field = browser.find_element_by_xpath("//input[@name='username']")
username_field.clear()
username_field.send_keys(username_1)
print('Entered username')
time.sleep(1)

#input password
password_field = browser.find_element_by_xpath("//input[@name='password']")
password_field.clear()
password_field.send_keys(password_1)
print('Entered password')
time.sleep(1)

#submit button
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()
print('Clicked submit')
time.sleep(3)


browser.get('https://www.instagram.com/p/CIbL_puJpRW/')

browser.find_element_by_tag_name('textarea')

try:

    browser.find_element_by_tag_name('textarea')
    print("Element exist")

except selenium.common.exceptions.NoSuchElementException:
    print("Element does not exist")

link = browser.find_element_by_class_name('sqdOP yWX7d     _8A5w5   ZIAjV ').get_attribute("href")

link2 = browser.find_element_by_partial_link_text('wildriftmobatr')

print(link2)












