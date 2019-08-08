'''
Created on Aug 6, 2019

@author: Rupesh
'''
from selenium import webdriver
#import webbrowser
from selenium.webdriver.common.keys import Keys
import time


url='https://login.salesforce.com/'
chrome_path='C:\\Users\\Rupesh\\Downloads\\chromedriver_win32\\chromedriver.exe'
firefox_path='C:\\Users\\Rupesh\\Downloads\\geckodriver-v0.24.0-win64\\geckodriver.exe'

driver= webdriver.Firefox(executable_path=r'C:\Users\Rupesh\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
driver.get(url)
driver.maximize_window()
time.sleep(2)

driver.find_element_by_id('forgot_password_link').click()
time.sleep(2)
driver.find_element_by_id('un').send_keys('pinky.ssingh1988-zmgn@force.com')
time.sleep(2)
driver.find_element_by_id('continue').click()
driver.quit()