from behave import given, when, then
from selenium.webdriver.common.by import By

TOP_LINKS = (By.CSS_SELECTOR, '#zg_tabs a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')


@given('Open Amazon Best Sellers')
def click_best_sellers_link(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab')


@when('Verify the best sellers {expected_links} link')
def verify_link_count(context, expected_links):
    actual_links = context.driver.find_elements(*TOP_LINKS)
    assert len(actual_links) == int(expected_links), f'Expected {expected_links} links, but got {len(actual_links)}'
    #context.driver.find_element(By.CSS_SELECTOR, "#zg_tabs")


@then('User can click on top links and verify that new page opens')
def click_top_links(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link = context.driver.find_elements(*TOP_LINKS)[x]

        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f' Expected {link_text} not in {header_text}'


