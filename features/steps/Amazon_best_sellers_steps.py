
from behave import given, then
from selenium.webdriver.common.by import By


@given('Open Amazon Best Sellers page')
def open_best_sellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers')


@then('Verify 5 links are displayed')
def verify_best_sellers_links(context):
    links = context.driver.find_elements(By.XPATH, "div#zg_tabs")
    print(links)
    assert len(links) == 5, f'Expected 5 links, but got {len(links)}'
