import cart as cart

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# init driver
driver = webdriver.Chrome(executable_path='/Users/mariamarques/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

search = driver.find_element(By.XPATH, '//*[@id="nav-cart"]')

search.send_keys('Cart icon', Keys.ENTER)

actual_text = driver.find_element(By.CSS_SELECTOR, 'a#nav-cart.nav-a.nav-a-2.nav-progressive-attribute').text
expected_text = 'Your Amazon Cart is empty'

driver.quit()

