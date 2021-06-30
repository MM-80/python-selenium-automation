

from behave import given, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Open Amazon wholefoods deals page')
def open_amazon_wholefoods(context):
    context.driver = webdriver.Chrome(executable_path='/Users/mariamarques/python-selenium-automation/chromedriver')
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify that every product has a text ‘Regular’ and a name')
def open_amazon_product(context):
    context.driver.implicitly_wait(15)
    context.driver.find_elements(By.CSS_SELECTOR, "div.a-section.a-padding-none.a-text-center.wfm-desktop-section-size div[class='s-item-container']")
    'Regular'



    # expected_text = "Maria   "
    # actual_text = "Maria   "
