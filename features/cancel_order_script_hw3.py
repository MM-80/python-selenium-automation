from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/Users/mariamarques/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')

search = driver.find_element(By.XPATH, '//*[@id="navFooter"]/div[1]/div/div[7]/ul/li[9]/a')

search.send_keys('help', Keys.ENTER)

search_field = driver.find_element(By.XPATH, '//*[@id="helpsearch"]')

search_field.send_keys('cancel order', Keys.ENTER)


driver.quit()

