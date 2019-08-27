from practice_2.asker_API import *
from practice_2.expert_portal import *


class RunTest:
    def run_test(self):
        asker = AskerAPI()
        expert = ExpertPortal()

        expert.login_facebook('honghaijumili206@gmail.com', 'bienhong206')
        asker.log_in('jasmine@gotitapp.co', '1234Aa')

        expert.start_working()
        problem_id = asker.post_question(-1000, '[Jasmine] I need a formula to combine column C with the numbers in columns L10 to L20')

        expert.wait_question_by_description(asker.question)
        asker.send_message(problem_id, 'thank you, next')
        print(expert.check_message(asker.message))


if __name__ == "__main__":
    run = RunTest()
    run.run_test()
