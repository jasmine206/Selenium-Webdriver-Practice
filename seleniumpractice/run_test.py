from seleniumpractice.asker_api import *
from seleniumpractice.expert_portal import *


class RunTest:
    def run_test(self):
        asker = AskerAPI()
        expert = ExpertPortal()

        expert.login_facebook(Config.EXPERT_EMAIL_LOGIN_FB, Config.EXPERT_PASSWORD_LOGIN_FB)
        asker.log_in(Config.ASKER_EMAIL_LOGIN, Config.ASKER_PASSWORD_LOGIN)

        expert.start_working()
        asker.post_question(Config.SUBJECT_ID, Config.ASKER_QUESTION)

        expert.wait_to_claim_question_by_title(Config.ASKER_QUESTION)
        assert (expert.is_in_session()), "Expert has lost the question"

        asker.send_message(asker.problem_id, Config.ASKER_MESSAGE)
        assert (expert.is_received_message(Config.ASKER_MESSAGE)), "Expert has not seen asker's API message"
        time.sleep(5)


if __name__ == "__main__":
    run = RunTest()
    run.run_test()
