from selenium.webdriver.common.by import By
from behave import given, when, then


@given('open Amazon help page')
def open_Amazon(context):
    context.deriver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input Cancel Order in search Help Library field')
def click_search(context):
    context.deriver.find_element(By.ID, 'helpsearch')


@when('tap enter')
def tap_enter(context):
    context.deriver.find_element(By.CLASS_NAME, 'a-icon-search').send_keys(Keys.ENTER)

@then('verify cancel item or order text is present')
def verify_search_worked(context):
    context.deriver.find_element(By.CLASS_NAME, 'a-icon-search').send_keys(Keys.ENTER)