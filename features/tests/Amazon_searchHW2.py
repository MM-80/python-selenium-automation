from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/mariamarques/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

search_field = driver.find_element(By.ID, 'helpsearch')

search_field.send_keys('cancel order')

driver.find_element(By.CLASS_NAME, 'a-icon-search').send_keys(Keys.ENTER)











