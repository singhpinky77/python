'''
Created on Aug 6, 2019

@author: Rupesh
'''
from selenium import webdriver
#import webbrowser
from selenium.webdriver.common.keys import Keys
import time
import gettext
url='https://login.salesforce.com/'
chrome_path='C:\\Users\\Rupesh\\Downloads\\chromedriver_win32\\chromedriver.exe'
firefox_path='C:\\Users\\Rupesh\\Downloads\\geckodriver-v0.24.0-win64\\geckodriver.exe'

driver= webdriver.Firefox(executable_path=r'C:\Users\Rupesh\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
driver.get(url)
driver.maximize_window()
time.sleep(4)


user = driver.find_element_by_id('username') 
user.send_keys('pinky.ssingh1988-zmgn@force.com')
driver.find_element_by_id('password').send_keys('1234Password') 
time.sleep(2)
driver.find_element_by_name('rememberUn').click()
driver.find_element_by_id('Login').click()
time.sleep(4)
#driver.find_element_by_xpath("//select[@name='Pinky Singh']/option[text()='Logout']").click()
#driver.find_element_by_xpath("//select[@id='userNavLabel']/option[@text='Logout']").click()
#driver.find_element_by_css_selector("select#userNavLabel > option[value='Logout']").click()
#select=driver.find_element_by_id("userNavLabel")
#select.select_by_visible_text('Logout')
driver.find_element_by_id('userNav-arrow').click()
time.sleep(2)
driver.find_element_by_link_text('Logout').click()
time.sleep(5)

driver.quit()