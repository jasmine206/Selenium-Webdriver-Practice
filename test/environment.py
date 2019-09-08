from behave import use_fixture

from test.fixtures import get_browser
from api.admin_api import AdminAPI
from driver import Driver


def before_tag(context, tag):
    if tag == 'chrome.browser':
        use_fixture(get_browser, context)


def after_tag(context, tag):
    if tag == 'expert.in.session':
        AdminAPI().terminate_session(context.asker_api.problem_id)


def before_scenario(context, scenario):
    context.scenario = scenario
    return context.scenario


def after_step(context, step):
    if step.status == "failed":
        Driver(context.browser).take_screenshot(step, context.scenario)
