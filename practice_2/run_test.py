from practice_2.asker_api import *
from practice_2.expert_portal import *


class RunTest:
    def run_test(self):
        asker = AskerAPI()
        expert = ExpertPortal()

        # Save accounts, url in a file to use for all files
        expert.login_facebook(Config.EXPERT_EMAIL_LOGIN_FB, Config.EXPERT_PASSWORD_LOGIN_FB)
        asker.log_in(Config.ASKER_EMAIL_LOGIN, Config.ASKER_PASSWORD_LOGIN)

        expert.start_working()
        asker.post_question(Config.SUBJECT_ID, Config.ASKER_QUESTION)

        expert.wait_to_claim_question_by_title(Config.ASKER_QUESTION)
        assert (expert.check_be_in_session()), "Expert has lost the question"
        asker.send_message(asker.problem_id, Config.ASKER_MESSAGE)
        assert (expert.check_message(Config.ASKER_MESSAGE)), "Expert has not seen asker's API message"
        time.sleep(3)


if __name__ == "__main__":
    run = RunTest()
    run.run_test()
