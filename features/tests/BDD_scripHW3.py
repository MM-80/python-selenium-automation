from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com')


@when('click on help icon')
def click_help_icon(context):
    context.driver.find_element(By.XPATH, '//*[@id="navFooter"]/div[1]/div/div[7]/ul/li[9]/a')


@when('Input Cancel Order in search the help library field')
def input_cancel_order(context):
    context.driver.find_element(By.XPATH, '//*[@id="helpsearch"]')


@then('Tap enter')
def tap_enter(context):
    context.driver.find_element(By.XPATH, '//*[@id="helpsearch"]')




