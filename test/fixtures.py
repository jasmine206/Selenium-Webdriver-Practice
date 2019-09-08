from behave import fixture

from driver_api import DriverAPI


@fixture
def get_browser(context):
    # Setup browser
    context.browser = DriverAPI().get_chrome_browser()

    yield context.browser

    # Teardown
    context.browser.quit()
