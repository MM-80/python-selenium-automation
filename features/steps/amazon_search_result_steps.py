from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon_page(context):
    #context.driver.get('https://www.amazon.com')
    context.app.main_page.open_main()


@when('Input Table in search field')
def search_amazon(context):
    #context.driver.find_element(By.ID, 'twotabsearchtextbox').snd('Table')
    context.app.header.input_search()


@when('Click on Amazon search icon')
def click_search(context):
    context.app.header.click_search()


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']").click()


@then('Verify search worked')
def verify_search_worked(context):
    #actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").click
    #expected_result = '"Table"'
    #assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
    context.app.search_results_page.verify_search_worked()