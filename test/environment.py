from behave import use_fixture

from config import Config
from test.fixtures import get_browser
from api.admin_api import AdminAPI
from driver_api import DriverAPI


def before_tag(context, tag):
    if tag == 'chrome.browser':
        use_fixture(get_browser, context)


def after_scenario(context, scenario):
    if context.problem_id is not None:
        AdminAPI().terminate_session_by_session_id(context.problem_id)


def before_scenario(context, scenario):
    context.scenario = scenario


def after_step(context, step):
    if step.status == "failed":
        DriverAPI(context.browser).take_screenshot(step, context.scenario, Config.screen_directory)
