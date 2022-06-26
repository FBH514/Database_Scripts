from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 2–––––––––––––––––––––––––

class Chapter_2(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 2
        self.chapter_name = "Data Models"
        self.numQuestions = 8

    @staticmethod
    def return_questions():
        q1 = Question_1()
        q2 = Question_2()
        q3 = Question_3()
        q4 = Question_4()
        q5 = Question_5()
        q6 = Question_6()
        q7 = Question_7()
        q8 = Question_8()

        question_list = [q1, q2, q3, q4, q5, q6, q7, q8]
        shuffle(question_list)
        return question_list


class Question_1(Chapter_2):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 2
        self.chapter_name = "Data Models"
        self.numQuestions = 8
        self.question = "What is an abstraction of a complex real-world data environment?"
        self.solution = "Data Model"
        self.description = "A data model is an abstraction of a complex real-world data environment. Database designers use data models to communicate with programmers and end users. The basic data-modeling components are entities, attributes, relationships, and constraints. Business rules are used to identify and define the basic modeling components within a specific real-world environment."


class Question_2(Chapter_2):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 2
        self.chapter_name = "Data Models"
        self.numQuestions = 8
        self.question = "Which model is the current database implementation standard?"
        self.solution = "Relational Model"
        self.description = "The relational model is the current database implementation standard. In the relational model, the end user perceives the data as being stored in tables. Tables are related to each other by means of common values in common attributes. The entity relationship (ER) model is a popular graphical tool for data modeling that complements the relational model. The ER model allows database designers to visually present different views of the data – as seen by database designers, programmers, and end users – and to to integrate the data into a common framework."


class Question_3(Chapter_2):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 2
        self.chapter_name = "Data Models"
        self.numQuestions = 8
        self.question = "What uses objects as the basic modeling structure?"
        self.solution = "OODM"
        self.description = "The object-oriented data model (OODM) uses objects as the basic modeling structure. Like the relational model's entity, an object is described by its factual content. Unlike an entity, however, the object also includes information about relationships between the facts, as well as relationships with other objects, thus giving its data more meaning."


class Question_4(Chapter_2):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 2
        self.chapter_name = "Data Models"
        self.numQuestions = 8
        self.question = "What are the new generation of databases that do not use the relational model and are geared to support the very specific needs of Big Data organizations?"
        self.solution = "NoSQL databases"
        self.description = "Big Data technologies such as Hadoop, MapReduce, and NoSQL provide distributed, fault-tolerant, and cost-efficient support for Big Data analytics. NoSQL databases are a new generation of databases that do not use the relational model and are geared to support the very specific needs of Big Data organizations. NoSQL databases offer distributed data stores that provide high scalability, availability, and fault tolerance by sacrificing data consistency and shifting the burden of maintaining relationships and data integrity to the program code."


class Question_5(Chapter_2):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.chapter = 2
        self.chapter_name = "Data Models"
        self.numQuestions = 8
        self.question = "What is the condition in which the internal model can be changed without affecting the conceptual model?"
        self.solution = "Logical Independence"
        self.description = "Logical independence is a condition in which the internal model CAN be changed without affecting the conceptual model. (The internal model is hardware-independent because it is unaffected by the computer on which the software is installed. Therefore, a change in storage devices or operating systems will mot affect the internal model."


class Question_6(Chapter_2):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.chapter = 2
        self.chapter_name = "Data Models"
        self.numQuestions = 8
        self.question = "What is the condition in which the physical model can be changed without affecting the internal model?"
        self.solution = "Physical Independence"
        self.description = "When you can change the physical model without affecting the internal model, you have physical independence. Therefore, a change in storage devices or methods and even a change in operating system will not affect the internal model."


class Question_7(Chapter_2):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.chapter = 2
        self.chapter_name = "Data Models"
        self.numQuestions = 8
        self.question = "What is a restriction placed on data?"
        self.solution = "Constraints"
        self.description = "Constraints are important because they help to ensure data integrity. Constraints are normally expressed in the form of rules."


class Question_8(Chapter_2):

    def __init__(self):
        super().__init__()
        self.numQ = 8
        self.chapter = 2
        self.chapter_name = "Data Models"
        self.numQuestions = 8
        self.question = "What are brief, precise and unambiguous descriptions of a policy, procedure or principle within a specific organization?"
        self.solution = "Business Rules"
        self.description = "Business rules derived from a detailed description of an organization's operations help to create and enforce actions within that organization's environment. Business rules must be rendered in writing and updated to reflect any change in the organization's operational environment."

# class Question_9(Chapter_2):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 9
#         self.question = ""
#         self.solution = ""
#         self.description = ""

# class Question_10(Chapter_2):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 10
#         self.question = ""
#         self.solution = ""
#         self.description = ""

# class Question_11(Chapter_2):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 11
#         self.question = ""
#         self.solution = ""
#         self.description = ""

# class Question_12(Chapter_2):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 12
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_13(Chapter_2):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 13
#         self.question = ""
#         self.solution = ""
#         self.description = ""
