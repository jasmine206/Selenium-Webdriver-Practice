from behave import use_fixture

from test.fixtures import get_chrome_browser


def before_tag(context, tag):
    if tag == 'chrome.browser':
        use_fixture(get_chrome_browser, context)
