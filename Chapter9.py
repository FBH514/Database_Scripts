from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 9–––––––––––––––––––––––––

class Chapter_9(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 9
        self.chapter_name = "Database Design"
        self.numQuestions = 3

    @staticmethod
    def return_questions():
        q1 = Question_1()
        q2 = Question_2()
        q3 = Question_3()

        question_list = [q1, q2, q3]
        shuffle(question_list)
        return question_list

class Question_1(Chapter_9):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 9
        self.chapter_name = "Database Design"
        self.numQuestions = 3
        self.question = "What is the process that establishes the need for an information system and its extent?"
        self.solution = "Systems analysis"
        self.description = "Systems analysis is the process that establishes the need for an information system and its extent. Systems development is the process of creating an information system."

class Question_2(Chapter_9):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 9
        self.chapter_name = "Database Design"
        self.numQuestions = 3
        self.question = "What traces the history of an application within the information system?"
        self.solution = "Systems Development Life Cycle | SDLC"
        self.description = "The Systems Development Life Cycle (SDLC) traces the history of an application within the information system. The SDLC can be divided into five phases: planning, analysis, detailed systems design, implementation, and maintenance. The SDLC is an iterative process rather than a sequential process."

class Question_3(Chapter_9):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 9
        self.chapter_name = "Database Design"
        self.numQuestions = 3
        self.question = "What describes the history of the database within the information system?"
        self.solution = "Database Life Cycle | DBLC"
        self.description = "The Database Life Cycle (DBLC) describes the history of the database within the information system. The DBLC is composed of six phases: database initial study, database design, implementation and loading, testing and evaluation, operation, and maintenance and evolution. Like the SDLC, the DBLC is iterative rather than sequential."
#
# class Question_4(Chapter_9):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 4
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_5(Chapter_9):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 5
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_6(Chapter_9):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 6
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_7(Chapter_9):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 7
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_8(Chapter_9):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 8
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_9(Chapter_9):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 9
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_10(Chapter_9):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 10
#         self.question = ""
#         self.solution = ""
#         self.description = ""
