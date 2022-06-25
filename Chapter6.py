from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 6–––––––––––––––––––––––––

class Chapter_6(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 6
        self.chapter_name = "Normalization of Database Tables"
        self.numQuestions = 7

    @staticmethod
    def return_questions():
        q1 = Question_1()
        q2 = Question_2()
        q3 = Question_3()
        q4 = Question_4()
        q5 = Question_5()
        q6 = Question_6()
        q7 = Question_7()

        question_list = [q1, q2, q3, q4, q5, q6, q7]
        shuffle(question_list)
        return question_list

class Question_1(Chapter_6):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 6
        self.chapter_name = "Normalization of Database Tables"
        self.numQuestions = 7
        self.question = "What is a technique used to design tables in which data redundancies are minimized."
        self.solution = "Normalization"
        self.description = "Normalization is a technique used to design tables in which data redundancies are minimized. The first three normal forms (1NF, 2NF, and 3NF) are the most com- mon. From a structural point of view, higher normal forms are better than lower normal forms because higher normal forms yield relatively fewer data redundancies in the database. Almost all business designs use 3NF as the ideal normal form."

class Question_2(Chapter_6):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 6
        self.chapter_name = "Normalization of Database Tables"
        self.numQuestions = 7
        self.question = "When all key attributes are defined and all remaining attributes are dependent on the primary key, which form is the table in?"
        self.solution = "1NF"
        self.description = "A table is in 1NF when all key attributes are defined and all remaining attributes are dependent on the primary key. However, a table in 1NF can still contain both partial and transitive dependencies."

class Question_3(Chapter_6):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 6
        self.chapter_name = "Normalization of Database Tables"
        self.numQuestions = 7
        self.question = "Name the dependency in which an attribute is functionally dependent on only a part of a multi-attribute primary key."
        self.solution = "Partial Dependency"
        self.description = "A partial dependency is one in which an attribute is functionally dependent on only a part of a multi-attribute primary key."

class Question_4(Chapter_6):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 6
        self.chapter_name = "Normalization of Database Tables"
        self.numQuestions = 7
        self.question = "Name the dependency is one in which an attribute is functionally dependent on another non-key attribute."
        self.solution = "Transitive Dependency"
        self.description = "A transitive dependency is one in which an attribute is functionally dependent on another non-key attribute."

class Question_5(Chapter_6):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.chapter = 6
        self.chapter_name = "Normalization of Database Tables"
        self.numQuestions = 7
        self.question = "When a contains no partial dependencies, which form is the table in?"
        self.solution = "2NF"
        self.description = "A table is in 2NF when it is in 1NF and contains no partial dependencies. Therefore, a 1NF table is automatically in 2NF when its primary key is based on only a single attribute. A table in 2NF may still contain transitive dependencies."

class Question_6(Chapter_6):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.chapter = 6
        self.chapter_name = "Normalization of Database Tables"
        self.numQuestions = 7
        self.question = "When a table contains no transitive dependency, which form is the table in?"
        self.solution = "3NF"
        self.description = "A table is in 3NF when it is in 2NF and contains no transitive dependencies."

class Question_7(Chapter_6):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.chapter = 6
        self.chapter_name = "Normalization of Database Tables"
        self.numQuestions = 7
        self.question = "What provides a way for the designer to check that the ERD meets a set of minimum requirements?"
        self.solution = "Data-modeling checklist"
        self.description = "The data-modeling checklist provides a way for the designer to check that the ERD meets a set of minimum requirements."

# class Question_8(Chapter_6):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 8
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_9(Chapter_6):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 9
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_10(Chapter_6):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 10
#         self.question = ""
#         self.solution = ""
#         self.description = ""
