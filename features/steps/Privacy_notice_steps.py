from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open Amazon T&C page')
def open_terms_conditions_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088 ')

    sleep(1)


@when('Store original windows')
def store_window(context):
    context.original_window = context.driver.current_window_handle

    sleep(1)


@when('Click on Amazon Privacy Notice link')
def click_amazon_pri_not_link(context):
    context.find_element(By.XPATH, "//a[@href='https://www.amazon.com/privacy']").click()

    sleep(1)


@when('Switch to the newly opened window')
def switch_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)

    sleep(1)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_not_page_is_opened(context):
    assert 'https://www.amazon.com/gp/help/customer/' in context.driver.current_url, f'Url https://www.amazon.com/gp/help/customer/ not in{context.driver.current_url}'

    sleep(1)


@then('User can close new window')
def close_window(context):
    context.driver.close()

    sleep(1)


@then('Switch back to original window')
def switch_to_original_window(context):
    original_window = context.driver.window_handle[1]
    context.driver.switch_to_window(original_window)

