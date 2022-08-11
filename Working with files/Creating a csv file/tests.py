from hstest import TestedProgram, CheckResult, StageTest, dynamic_test
import os

FILENAME = 'numbers.csv'


class CheckDeletedFileTest(StageTest):
    @dynamic_test
    def test_1(self):
        # TestedProgram() helps runs the _main.go_ file so it can execute `os.Create()`
        pr = TestedProgram()
        pr.start()

        if os.path.exists(os.getcwd() + f"{os.path.sep}{FILENAME}"):
            print("\033[1;35m")
            print(f"The file {FILENAME} has been created!")
            return CheckResult.correct()

        else:
            return CheckResult.wrong(f"Error! Make sure you create {FILENAME} and not any other file!")


if __name__ == '__main__':
    if os.path.exists(os.getcwd() + f"{os.path.sep}{FILENAME}"):
        os.remove(os.getcwd() + f"{os.path.sep}{FILENAME}")
    CheckDeletedFileTest().run_tests()
