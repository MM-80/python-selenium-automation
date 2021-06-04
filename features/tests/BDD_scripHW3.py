from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')


@when('click on help icon')
def click_help_icon(context):
    search = context.driver.find_element(By. ID, 'a.nav_a').send_key('Click')


@when('Input Cancel Order')
def input_cancel_order(context):
    context.driver.find_element(By.ID, 'a.nav_a').click()


@and('Tap enter')
def tap_enter(context):
    context.driver.find_element(By.ID, 'a.nav_a').click()
