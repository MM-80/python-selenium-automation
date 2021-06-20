from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@when('click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By. CSS_SELECTOR, 'a#nav-cart.nav-a.nav-a-2.nav-progressive-attribute').send_key('Click')


@then('verify that is empty')
def verify_is_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, 'h2.sc-your-amazon-cart-is-empty').click()
