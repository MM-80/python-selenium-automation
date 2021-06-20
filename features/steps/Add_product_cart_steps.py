import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input pencils on search field')
def search_product(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('pencils', Keys.ENTER)


@when('Click on the first product')
def click_first_product(context):
    time.sleep(2)
    all_product_links = context.driver.find_elements(By.XPATH, "//a[@class='a-link-normal a-text-normal']")
    print(len(all_product_links))


@when('Click on add to cart button')
def click_add_cart_button(context):
    context.driver.find_elements(By.XPATH, '//*[@id="add-to-cart-button"]')


@then('Verify cart has one item')
def item_on_cart(context):
    actual_result = context.driver.find_element(By. XPATH, '//*[@id="nav-cart-count"]')
    print(actual_result.text)


