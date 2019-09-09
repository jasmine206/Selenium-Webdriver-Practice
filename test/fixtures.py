from behave import fixture

from selenium_driver import SeleniumDriver


@fixture
def get_browser(context):
    # Setup browser
    context.browser = SeleniumDriver().get_chrome_browser()

    yield context.browser

    # Teardown
    context.browser.quit()
