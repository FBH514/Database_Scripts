import time
from random import shuffle
import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5
import Chapter6
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
        self.chapters = [Chapter_1(), Chapter_2(), Chapter_3(), Chapter_4(), Chapter_5(), Chapter_6()]

        # list all questions from every chapter
        self.questions = [Chapter1.Question_1,
                          Chapter1.Question_2,
                          Chapter1.Question_3,
                          Chapter1.Question_4,
                          Chapter1.Question_5,
                          Chapter1.Question_6,
                          Chapter1.Question_7,
                          Chapter1.Question_8,
                          Chapter1.Question_9,
                          Chapter1.Question_10,
                          Chapter2.Question_1,
                          Chapter2.Question_2,
                          Chapter2.Question_3,
                          Chapter2.Question_4,
                          Chapter2.Question_5,
                          Chapter2.Question_6,
                          Chapter2.Question_7,
                          Chapter2.Question_8,
                          Chapter3.Question_1,
                          Chapter3.Question_2,
                          Chapter3.Question_3,
                          Chapter3.Question_4,
                          Chapter3.Question_5,
                          Chapter3.Question_6,
                          Chapter3.Question_7,
                          Chapter4.Question_1,
                          Chapter4.Question_2,
                          Chapter4.Question_3,
                          Chapter4.Question_4,
                          Chapter4.Question_5,
                          Chapter4.Question_6,
                          Chapter4.Question_7,
                          Chapter4.Question_8,
                          Chapter4.Question_9,
                          Chapter5.Question_1,
                          Chapter5.Question_2,
                          Chapter5.Question_3,
                          Chapter5.Question_4,
                          Chapter5.Question_5,
                          Chapter5.Question_6,
                          Chapter5.Question_7,
                          Chapter5.Question_8,
                          Chapter5.Question_9,
                          Chapter5.Question_10,
                          Chapter6.Question_1,
                          Chapter6.Question_2,
                          Chapter6.Question_3,
                          Chapter6.Question_4,
                          Chapter6.Question_5,
                          Chapter6.Question_6,
                          Chapter6.Question_7]

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
            if self.user_input("Do you want a fixed length mock exam? Y/N ––> ") == "Y".casefold():
                print("You have chosen to take a fixed length mock exam")
                questions = self.user_input("How many questions do you want to answer? --> ")
                if questions.isdigit():
                    length = int(questions)
                    if length > 0:
                        shuffle(self.questions)
                        for item in range(length):
                            exam.append(self.questions[item])
                        return exam

            else:
                chapter = self.user_input("Enter the chapter number you want to take ––> ")
                if chapter.isdigit():
                    return int(chapter) - 1

    # run the program
    def main(self):
        print()
        print("Welcome to the Database Class Exam")
        global_counter = 0
        self.question_count = 0

        # exam = self.exam_style()
        # if type(exam) == list:
        #     target = self.questions
        #     print(len(target))
        #
        # elif type(exam) == int:
        #     target = self.chapters[exam]

        # for chapter in range(self.exam_style()):
        #     global_counter += 1
        
        target = self.chapters[self.exam_style()]
        for item in target.return_questions():
            self.question_count += 1
            print("\n")
            print(
                f"** You are taking Chapter {target.chapter} with {target.numQuestions - self.question_count} questions left **")
            print(
                f"Chapter {target.chapter} | {target.chapter_name}\n\nQuestion {item.numQ} | {item.question}")

            while True:
                if self.user_input("Enter your answer ––> ") in item.solution.casefold():
                    print("\n")
                    self.grade_count += 1
                    target.grade(self.grade_count)
                    print(f"\nSolution to Chapter {target.chapter}, Question {item.numQ} ––> {item.solution} ")
                    print(f"More info about * {item.solution} *\n{item.description}")
                    print("\n")
                    print(self.template.compliments())
                    self.template.beautify(20)

                else:
                    print("\n")
                    print(f"Solution to Chapter {target.chapter}, Question {item.numQ} ––> {item.solution} ")
                    print(f"More info about * {item.solution} *\n{item.description}")
                    print("\n")
                    print(self.template.invalid_answer())
                    self.template.beautify(20)
                break

            while True:
                correction = self.user_input("\nDo you want to manually correct your answer? Y/N ––> ")
                if correction == "Y".casefold() or correction == "Yes".casefold():
                    print(f"{self.template.compliments()} | +1 towards your grade")
                    self.grade_count += 1
                    target.grade(self.grade_count)
                elif correction == "N".casefold() or correction == "No".casefold():
                    print("No correction needed")
                else:
                    print("Invalid input")
                    continue
                break

            self.template.beautify(len("No correction needed"))

        print(f"\nYou scored {self.grade_count}/{target.numQuestions} ––> {target.grade(self.grade_count)}")
        self.template.beautify(20)

        while True:
            run_again = self.user_input("Do you want to run the program again? Y/N ––> ")
            if run_again == "Y".casefold() or run_again == "Yes".casefold():
                self.question_count = 0
                self.grade_count = 0
                self.main()
            elif run_again == "N".casefold() or run_again == "No".casefold():
                print("** Ending Program **")
                break


if __name__ == "__main__":
    main = Main()
    main.main()



        # print("You have answered {} out of {} questions".format(self.question_count, len(exam)))
        # for chapter in range(len(self.exam_style())):
