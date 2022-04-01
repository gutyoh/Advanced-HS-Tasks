import os

from hstest import StageTest, CheckResult, WrongAnswer, TestCase

SHA512_output = ["025439534d144f2b3bce2df5a05a249087997a824841258f9b788ebb9e5b5579335a14fcb2ebc66a371f951bc4414865e898522b14975c3af990b69514765906"]

FILENAME = "secret_formula.txt"


class TestAdmissionProcedure(StageTest):
    def generate(self):
        return [TestCase(stdin=[test], attach=[test]) for test in SHA512_output]

    def check(self, reply: str, clue: str):
        if not os.path.exists(FILENAME):
            raise WrongAnswer(f"Cannot find file {FILENAME}")

        if clue[0].rstrip() != reply.rstrip():
            raise WrongAnswer(
                f"Incorrect! 😵❌ Wrong answer!\n"
                f"Your program printed:\n{reply.rstrip()}\n"
                f"\nAre you sure you properly opened {FILENAME}?")

        print(f"\nWell done! Mr. Krabs says thanks!\n")
        return CheckResult.correct()

if __name__ == '__main__':
    TestAdmissionProcedure().run_tests()