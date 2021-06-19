import time

from behave import given, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Open amazon product B081YS2F7N page')
def open_amazon_product(context):
    context.driver = webdriver.Chrome(executable_path='/Users/mariamarques/python-selenium-automation/chromedriver')
    context.driver.get('https://www.amazon.com/dp/B081YS2F7N')


@then('Verify user can loop through colors')
def verify_can_loop_thru_colors(context):
    expected_colors = ['Black', 'Blue', 'Burgundy', 'Grey', 'Green', 'Khaki', 'Pink', 'White', 'Yellow']
    color_webelements = context.driver.find_elements(By. CSS_SELECTOR, '#variation_color_name li')

    for i in range(len(color_webelements)):
        color_webelements[i].click()
        time.sleep(2)
        actual_text = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name span.selection").text
