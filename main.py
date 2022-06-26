import time
from random import shuffle
import Chapter1
import Chapter10
import Chapter11
import Chapter12
import Chapter13
import Chapter14
import Chapter15
import Chapter16
import Chapter2
import Chapter3
import Chapter4
import Chapter5
import Chapter6
import Chapter7
import Chapter8
import Chapter9
from Template import *
from Chapter1 import Chapter_1
from Chapter2 import Chapter_2
from Chapter3 import Chapter_3
from Chapter4 import Chapter_4
from Chapter5 import Chapter_5
from Chapter6 import Chapter_6
from Chapter7 import Chapter_7
from Chapter8 import Chapter_8
from Chapter9 import Chapter_9
from Chapter10 import Chapter_10
from Chapter11 import Chapter_11
from Chapter12 import Chapter_12
from Chapter13 import Chapter_13
from Chapter14 import Chapter_14
from Chapter15 import Chapter_15
from Chapter16 import Chapter_16


class Main:
    def __init__(self):
        # init the grade counter
        self.grade_count = 0

        # inits the question counter
        self.question_count = 0

        # create instance of Template class
        self.template = Template()

        # create instance of all Chapter classes
        self.chapters = [Chapter_1(), Chapter_2(), Chapter_3(), Chapter_4(), Chapter_5(), Chapter_6(), Chapter_7(),
                         Chapter_8(), Chapter_9(), Chapter_10(), Chapter_11(), Chapter_12(), Chapter_13(), Chapter_14(),
                         Chapter_15(), Chapter_16()]

        # list all questions from every chapter
        self.questions = [Chapter1.Question_1(),
                          Chapter1.Question_2(),
                          Chapter1.Question_3(),
                          Chapter1.Question_4(),
                          Chapter1.Question_5(),
                          Chapter1.Question_6(),
                          Chapter1.Question_7(),
                          Chapter1.Question_8(),
                          Chapter1.Question_9(),
                          Chapter1.Question_10(),
                          Chapter2.Question_1(),
                          Chapter2.Question_2(),
                          Chapter2.Question_3(),
                          Chapter2.Question_4(),
                          Chapter2.Question_5(),
                          Chapter2.Question_6(),
                          Chapter2.Question_7(),
                          Chapter2.Question_8(),
                          Chapter3.Question_1(),
                          Chapter3.Question_2(),
                          Chapter3.Question_3(),
                          Chapter3.Question_4(),
                          Chapter3.Question_5(),
                          Chapter3.Question_6(),
                          Chapter3.Question_7(),
                          Chapter4.Question_1(),
                          Chapter4.Question_2(),
                          Chapter4.Question_3(),
                          Chapter4.Question_4(),
                          Chapter4.Question_5(),
                          Chapter4.Question_6(),
                          Chapter4.Question_7(),
                          Chapter4.Question_8(),
                          Chapter4.Question_9(),
                          Chapter5.Question_1(),
                          Chapter5.Question_2(),
                          Chapter5.Question_3(),
                          Chapter5.Question_4(),
                          Chapter5.Question_5(),
                          Chapter5.Question_6(),
                          Chapter5.Question_7(),
                          Chapter5.Question_8(),
                          Chapter5.Question_9(),
                          Chapter5.Question_10(),
                          Chapter6.Question_1(),
                          Chapter6.Question_2(),
                          Chapter6.Question_3(),
                          Chapter6.Question_4(),
                          Chapter6.Question_5(),
                          Chapter6.Question_6(),
                          Chapter6.Question_7(),
                          Chapter7.Question_1(),
                          Chapter7.Question_2(),
                          Chapter7.Question_3(),
                          Chapter7.Question_4(),
                          Chapter7.Question_5(),
                          Chapter7.Question_6(),
                          Chapter7.Question_7(),
                          Chapter7.Question_8(),
                          Chapter7.Question_9(),
                          Chapter7.Question_10(),
                          Chapter7.Question_11(),
                          Chapter8.Question_1(),
                          Chapter8.Question_2(),
                          Chapter8.Question_3(),
                          Chapter8.Question_4(),
                          Chapter8.Question_5(),
                          Chapter8.Question_6(),
                          Chapter8.Question_7(),
                          Chapter8.Question_8(),
                          Chapter8.Question_9(),
                          Chapter8.Question_10(),
                          Chapter9.Question_1(),
                          Chapter9.Question_2(),
                          Chapter9.Question_3(),
                          Chapter10.Question_1(),
                          Chapter10.Question_2(),
                          Chapter10.Question_3(),
                          Chapter10.Question_4(),
                          Chapter10.Question_5(),
                          Chapter10.Question_6(),
                          Chapter10.Question_7(),
                          Chapter10.Question_8(),
                          Chapter10.Question_9(),
                          Chapter10.Question_10(),
                          Chapter10.Question_11(),
                          Chapter10.Question_12(),
                          Chapter10.Question_13(),
                          Chapter11.Question_1(),
                          Chapter11.Question_2(),
                          Chapter11.Question_3(),
                          Chapter11.Question_4(),
                          Chapter11.Question_5(),
                          Chapter11.Question_6(),
                          Chapter11.Question_7(),
                          Chapter11.Question_8(),
                          Chapter11.Question_9(),
                          Chapter12.Question_1(),
                          Chapter12.Question_2(),
                          Chapter12.Question_3(),
                          Chapter12.Question_4(),
                          Chapter12.Question_5(),
                          Chapter12.Question_6(),
                          Chapter12.Question_7(),
                          Chapter12.Question_8(),
                          Chapter13.Question_1(),
                          Chapter13.Question_2(),
                          Chapter13.Question_3(),
                          Chapter13.Question_4(),
                          Chapter13.Question_5(),
                          Chapter13.Question_6(),
                          Chapter13.Question_7(),
                          Chapter13.Question_8(),
                          Chapter14.Question_1(),
                          Chapter14.Question_2(),
                          Chapter14.Question_3(),
                          Chapter14.Question_4(),
                          Chapter15.Question_1(),
                          Chapter15.Question_2(),
                          Chapter15.Question_3(),
                          Chapter16.Question_1(),
                          Chapter16.Question_2(),
                          Chapter16.Question_3(),
                          Chapter16.Question_4(),
                          Chapter16.Question_5(),
                          Chapter16.Question_6(),
                          Chapter16.Question_7()]

    # gets user input
    @staticmethod
    def user_input(question):
        while True:
            user_input = input(question)
            if len(user_input) > 0:
                return user_input
            else:
                print("Invalid input")
                continue

    # choose your exam style
    def exam_style(self):
        print("Choose your exam style")
        self.template.beautify(20)
        exam = []
        while True:
            if self.user_input("Do you want a fixed length mock exam? Y/N ––> ").casefold() == "Y".casefold():
                print("You have chosen to take a fixed length mock exam")
                questions = self.user_input("How many questions do you want to answer? --> ")
                if questions.isdigit():
                    length = int(questions)
                    if 0 < length <= len(self.questions):
                        shuffle(self.questions)
                        for item in range(length):
                            exam.append(self.questions[item])
                        return exam
                    else:
                        print("The exam length is invalid –– {} questions are available".format(len(self.questions)))
                        continue
                else:
                    continue

            else:
                chapter = self.user_input("Enter the chapter number you want to take ––> ")
                if chapter.isdigit():
                    return int(chapter) - 1
                else:
                    print("Invalid input")
                    continue

    # run the program
    def main(self):
        print("\n")
        print("Welcome to the Database Class Exam")
        self.question_count = 0

        # get the exam style
        exam = self.exam_style()
        if type(exam) == list:
            target = exam
        elif type(exam) == int:
            hey = self.chapters[exam]
            target = hey.return_questions()

        # run the exam
        for item in target:
            print("\n")
            print("** Your exam has {} questions left **".format(len(target) - self.question_count))
            self.question_count += 1
            print(
                f"Chapter {item.chapter} | {item.chapter_name}\n\nQuestion {item.numQ} | {item.question}")

            # get the user input + check if it is correct
            while True:
                if self.user_input("\nEnter your answer ––> ") in item.solution.casefold():
                    print("\n")
                    self.grade_count += 1
                    item.grade(self.grade_count)
                    print(f"\nSolution to Chapter {item.chapter}, Question {item.numQ} ––> {item.solution} ")
                    print(f"More info about * {item.solution} *\n{item.description}")
                    print("\n")
                    print(self.template.compliments())
                    self.template.beautify(20)

                else:
                    print("\n")
                    print(f"Solution to Chapter {item.chapter}, Question {item.numQ} ––> {item.solution} ")
                    print(f"More info about * {item.solution} *\n{item.description}")
                    print("\n")
                    print(self.template.invalid_answer())
                    self.template.beautify(20)

                    # manual correction in case of typo or wrong solution
                    while True:
                        correction = self.user_input("\nDo you want to manually correct your answer? Y/N ––> ")
                        if correction.casefold() == "Y".casefold() or correction.casefold() == "Yes".casefold():
                            print(f"{self.template.compliments()} | +1 towards your grade")
                            self.grade_count += 1
                            item.grade(self.grade_count)
                        elif correction.casefold() == "N".casefold() or correction.casefold() == "No".casefold():
                            print("No correction needed")
                        else:
                            print("Invalid input")
                            continue
                        break
                    self.template.beautify(20)
                break

            # self.template.beautify(len("No correction needed"))

        item.numQuestions = self.question_count  # resets the final number of questions
        print(f"\nYou scored {self.grade_count}/{len(target)} ––> {item.grade(self.grade_count)}")
        self.template.beautify(20)

        # asks user if they want to take a new exam
        while True:
            run_again = self.user_input("Do you want to run the program again? Y/N ––> ")
            if run_again.casefold() == "Y".casefold() or run_again.casefold() == "Yes".casefold():
                self.question_count = 0
                self.grade_count = 0
                self.main()
            elif run_again.casefold() == "N".casefold() or run_again.casefold() == "No".casefold():
                print("** Ending Program **")
                break
        print("\n")


if __name__ == "__main__":
    main = Main()
    main.main()
