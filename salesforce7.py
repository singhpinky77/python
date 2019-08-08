'''
Created on Aug 7, 2019

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
pwd=driver.find_element_by_id('password')
pwd.send_keys('1234Password') 
time.sleep(2)
driver.find_element_by_id('Login').click()
time.sleep(5)

driver.find_element_by_id('Opportunity_Tab').click()
driver.find_element_by_id('fcf').click()
time.sleep(5)

driver.quit()