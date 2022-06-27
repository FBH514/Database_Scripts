from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 15–––––––––––––––––––––––––
class Chapter_15(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 15
        self.chapter_name = "Database Connectivity and Web Technologies"
        self.numQuestions = 3

    @staticmethod
    def return_questions():
        q1 = Question_1()
        q2 = Question_2()
        q3 = Question_3()

        question_list = [q1, q2, q3]
        shuffle(question_list)
        return question_list

class Question_1(Chapter_15):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 15
        self.chapter_name = "Database Connectivity and Web Technologies"
        self.numQuestions = 3
        self.question = "What refers to the mechanisms through which application programs connect and communicate with data repositories?"
        self.solution = "Database Connectivity"
        self.description = "Database connectivity refers to the mechanisms through which application programs connect and communicate with data repositories. Database connectivity software is also known as database middleware."

class Question_2(Chapter_15):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 15
        self.chapter_name = "Database Connectivity and Web Technologies"
        self.numQuestions = 3
        self.question = "What facilitates the exchange of B2B and other data over the internet?"
        self.solution = "XML"
        self.description = "XML facilitates the exchange of B2B and other data over the internet. XML provides the semantics that facilitate the exchange, sharing, and manipulation of structured documents across organizational boundaries. XML produces the description and the representation of data, thus setting the stage for data manipulation in ways that were not possible before. XML documents can be validated through the use of document type definition documents and XML schema documents."

class Question_3(Chapter_15):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 15
        self.chapter_name = "Database Connectivity and Web Technologies"
        self.numQuestions = 3
        self.question = "What is a computing model that provides ubiquitous, on-demand access to a shared pool of configurable resources that can be rapidly provisioned?"
        self.solution = "Cloud Computing"
        self.description = "Cloud computing is a computing model that provides ubiquitous, on-demand access to a shared pool of configurable resources that can be rapidly provisioned."

# class Question_4(Chapter_15):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 4
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_5(Chapter_15):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 5
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_6(Chapter_15):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 6
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_7(Chapter_15):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 7
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_8(Chapter_15):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 8
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_9(Chapter_15):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 9
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_10(Chapter_15):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 10
#         self.question = ""
#         self.solution = ""
#         self.description = ""
