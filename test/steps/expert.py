import time

from behave import *
from api.asker_api import *
from config import Config
from pom.landing_page import LandingPage
from pom.home_page import HomePage
from pom.work_space import WorkSpace
from pom.facebook import FacebookVerification
from pom.bidding_screen import BiddingScreen
from pom.working_screen import WorkingScreen


@given("I am at expert landing page")
def step_impl(context):
    context.browser.get(Config.EXPERT_BASE_URL)


@given("I log in with Facebook")
def step_impl(context):
    landing_page = LandingPage(context.browser)
    parent_handle = landing_page.login_facebook()

    facebook_verification = FacebookVerification(context.browser)
    facebook_verification.log_in(parent_handle, Config.EXPERT_EMAIL_LOGIN_FB, Config.EXPERT_PASSWORD_LOGIN_FB)


@when("An asker log in")
def step_impl(context):
    context.asker_api = AskerAPI()
    context.asker_api.log_in(Config.ASKER_EMAIL_LOGIN, Config.ASKER_PASSWORD_LOGIN)


@when("I click on START WORKING button")
def step_impl(context):
    home_page = HomePage(context.browser)
    home_page.start_working()


@when("Asker posts a question")
def step_impl(context):
    context.asker_api.post_question(Config.SUBJECT_ID, Config.ASKER_QUESTION)


@when("I wait to claim question the question that asker've posted")
def step_impl(context):
    bidding_screen = BiddingScreen(context.browser)
    bidding_screen.wait_to_claim_question_by_title(Config.ASKER_QUESTION)


@when("I win the question")
def step_impl(context):
    working_screen = WorkingScreen(context.browser)
    assert (working_screen.is_in_session()), "Expert has lost the question"


@when("Asker sends {message}")
def step_impl(context, message):
    if message == 'text':
        context.asker_api.send_text_message(context.asker_api.problem_id, Config.ASKER_MESSAGE)
    elif message == 'image':
        context.asker_api.send_image_message(context.asker_api.problem_id, Config.ASKER_IMAGE_PATH)
    elif message == 'excel file':
        context.asker_api.send_excel_file_message(context.asker_api.problem_id, Config.ASKER_EXCEL_FILE_PATH)
    else:
        print('Message type is not supported')


@then("I should see asker's {message}")
def step_impl(context, message):
    expert_portal_po = WorkSpace(context.browser)
    if message == 'text':
        assert (expert_portal_po.is_received_text_message(Config.ASKER_MESSAGE)),\
            "Expert has not seen asker's API message"
    elif message == 'image':
        assert (expert_portal_po.is_received_text_message(Config.ASKER_MESSAGE)), \
            "Expert has not seen asker's API message"
    elif message == 'excel file':
        assert (expert_portal_po.is_received_text_message(Config.ASKER_MESSAGE)), \
            "Expert has not seen asker's API message"
    else:
        print('Message type is not supported')
    time.sleep(3)
