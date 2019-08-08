'''
Created on Aug 5, 2019

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
time.sleep(2)

user = driver.find_element_by_id('username') 

user.send_keys('singhpinky77@gmail.com')
driver.find_element_by_id('password').send_keys('') 
time.sleep(4)
driver.find_element_by_id('Login').click()
time.sleep(2)

errormsg=driver.find_element_by_id('error')

if errormsg.text=="Please enter your password.":
    print('Error msg is showing')
else:
    print('Msg is not showing')

time.sleep(2)
driver.quit()