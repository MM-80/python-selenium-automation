from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input pencils on search field')
def search_product(context):
    context.drever.find_element(By. ID, 'twotabsearchtextbox').send_keys('pencils')


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(By. XPATH, '//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[2]/div/span/div/div/div/div/span/a/div/img').click()


@when('Click on add to cart button')
def click_add_cart_button(context):
    context.driver.find_element(By. XPATH, '//*[@id="add-to-cart-button"]').click()


@then('Verify cart has one item')
def item_on_cart(context):
    actual_result = context.driver.find_element(By. XPATH, '//*[@id="nav-cart-count"]')
    expected_result = "pencils"

    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'

    context.driver.quit()





