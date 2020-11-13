#pip install selenium

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# open the Google Chrome browser
driver = webdriver.Chrome()

# maximize the window browser
driver.maximize_window()

# remove the cookies
driver.delete_all_cookies()

# go to URL
driver.get('https://www.gmail.com')

# identify user name 
driver.find_element_by_id("identifierid").send_keys('insert_your_email')

time.sleep(2)

# click Next
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()

time.sleep(3)

# identify password
driver.find_element_by_name('password').send_keys("#########")
time.sleep(3)

# click Next
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
time.sleep(3)

# close the browser
driver.close()
print('Gmail account has been logged in')