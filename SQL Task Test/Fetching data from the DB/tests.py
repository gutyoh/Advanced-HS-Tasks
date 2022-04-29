from hstest import StageTest, CheckResult, WrongAnswer, TestCase

query_output = ["1 Rock\n2 Jazz\n3 Metal\n4 Alternative & Punk\n5 Rock And Roll\n\
6 Blues\n7 Latin\n8 Reggae\n9 Pop\n10 Soundtrack\n\
11 Bossa Nova\n12 Easy Listening\n13 Heavy Metal\n14 R&B/Soul\n15 Electronica/Dance\n\
16 World\n17 Hip Hop/Rap\n18 Science Fiction\n19 TV Shows\n20 Sci Fi & Fantasy\n\
21 Drama\n22 Comedy\n23 Alternative\n24 Classical\n25 Opera\n"]


class TestAdmissionProcedure(StageTest):
    def generate(self):
        return [TestCase(stdin=[test], attach=[test]) for test in query_output]

    def check(self, reply, clue):
        if reply != clue[0]:
            return CheckResult.wrong(
                "Wrong answer! 😵❌ Wrong answer!\n"
                "Your program printed:\n{}\nExpected:\n{}".format(reply, clue[0]))

        return CheckResult.correct()


if __name__ == '__main__':
    TestAdmissionProcedure().run_tests()
