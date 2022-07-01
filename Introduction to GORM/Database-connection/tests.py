from hstest import StageTest, CheckResult, WrongAnswer, TestCase

import os

FILENAME = "chinook.db"

class Test(StageTest):
    def generate(self):
        return [TestCase(stdin="", attach="Successfully established a connection to chinook.db")]

    def check(self, reply, attach):
        if not os.path.exists(FILENAME):
            raise WrongAnswer(f"Wrong! Make sure you're trying to connect to \"{FILENAME}\"")

        if reply.strip() == "Successfully established a connection to chinook.db":
            return CheckResult.correct()
        else:
            return CheckResult.wrong(f'Your answer is {reply}\nExpected {attach}')


if __name__ == '__main__':
    Test().run_tests()
