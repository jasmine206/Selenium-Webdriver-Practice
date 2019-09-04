from behave import *
from seleniumpractice.asker_api import *
from seleniumpractice.expert_portal import *

use_step_matcher("re")


asker = AskerAPI()
expert = ExpertPortal()


@given("I am an expert")
def login_expert(context):
    expert.login_facebook(Config.EXPERT_EMAIL_LOGIN_FB, Config.EXPERT_PASSWORD_LOGIN_FB)


@when("An asker log in")
def login_asker_api(context):
    asker.log_in(Config.ASKER_EMAIL_LOGIN, Config.ASKER_PASSWORD_LOGIN)


@when("I start working")
def start_working(context):
    expert.start_working()


@when("Asker posts a question")
def post_question_api(context):
    asker.post_question(Config.SUBJECT_ID, Config.ASKER_QUESTION)


@when("I wait to claim question")
def wait_to_claim_question_by_title(context):
    expert.wait_to_claim_question_by_title(Config.ASKER_QUESTION)


@when("I win the question")
def is_in_session(context):
    assert (expert.is_in_session()), "Expert has lost the question"


@when("Asker sends a message")
def send_message_api(context):
    asker.send_message(asker.problem_id, Config.ASKER_MESSAGE)


@then("Then I should see asker's message")
def is_received_message(context):
    assert (expert.is_received_message(Config.ASKER_MESSAGE)), "Expert has not seen asker's API message"
    time.sleep(3)
