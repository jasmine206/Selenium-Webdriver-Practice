from behave import *
from api.asker_api import *
from pom.expert_portal import *
from config import Config


@given("I am at landing page")
def step_impl(context):
    context.browser.get(Config.EXPERT_BASE_URL)


@given("I am an expert")
def step_impl(context):
    expert_portal_po = ExpertPortal(context.browser)
    expert_portal_po.login_facebook(Config.EXPERT_EMAIL_LOGIN_FB, Config.EXPERT_PASSWORD_LOGIN_FB)


@when("An asker log in")
def step_impl(context):
    context.asker = AskerAPI()
    context.asker.log_in(Config.ASKER_EMAIL_LOGIN, Config.ASKER_PASSWORD_LOGIN)


@when("I start working")
def step_impl(context):
    expert_portal_po = ExpertPortal(context.browser)
    expert_portal_po.start_working()


@when("Asker posts a question")
def step_impl(context):
    context.asker.post_question(Config.SUBJECT_ID, Config.ASKER_QUESTION)


@when("I wait to claim question")
def step_impl(context):
    expert_portal_po = ExpertPortal(context.browser)
    expert_portal_po.wait_to_claim_question_by_title(Config.ASKER_QUESTION)


@when("I win the question")
def step_impl(context):
    expert_portal_po = ExpertPortal(context.browser)
    assert (expert_portal_po.is_in_session()), "Expert has lost the question"


@when("Asker sends a message")
def step_impl(context):
    context.asker.send_message(context.asker.problem_id, Config.ASKER_MESSAGE)


@then("Then I should see asker's message")
def step_impl(context):
    expert_portal_po = ExpertPortal(context.browser)
    assert (expert_portal_po.is_received_message(Config.ASKER_MESSAGE)), "Expert has not seen asker's API message"
    time.sleep(3)
