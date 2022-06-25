from Template import Template
from random import shuffle
# when adding questions, update numQuestions and return_questions


# –––––––––––––––––––––––––Chapter 4–––––––––––––––––––––––––

class Chapter_4(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 4
        self.chapter_name = "Entity Relationship (ER) Modeling"
        self.numQuestions = 9

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
        q9 = Question_9()

        question_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9]
        shuffle(question_list)
        return question_list


class Question_1(Chapter_4):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.question = "What uses ERDs to represent the conceptual database as viewed by the end user?"
        self.solution = "ERM"
        self.description = "The Entity-Relationship Model (ERM) uses ERDs to represent the conceptual database as viewed by the end user. The ERM’s main components are entities, relationships, and attributes. The ERD includes connectivity and cardinality notations, and can also show relationship strength, relationship participation (optional or mandatory), and degree of relation- ship (such as unary, binary, or ternary)."

class Question_2(Chapter_4):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.question = "What describes the relationship classification (1:1, 1:M, or M:N)?"
        self.solution = "Connectivity"
        self.description = "A relationship in a DBMS, is primarily the way two or more data sets are linked. This is so true for Relational Database Management Systems. One dataset may be then termed as the Foreign key and the ones linked to it may be termed as the Primary Key. There may be multiple Foreign and Primary keys linked to each other."

class Question_3(Chapter_4):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.question = "What expresses the specific number of occurrences associated with an occurrence of a related entity?"
        self.solution = "Cardinality"
        self.description = "A property that assigns a specific value to connectivity and expresses the range of allowed entity occurrences associated with a single occurrence of the related entity."

class Question_4(Chapter_4):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.question = "Which class diagrams are used to represent the static data structures in a data model?"
        self.solution = "UML"
        self.description = "UML, which stands for Unified Modeling Language, is a way to visually represent the architecture, design, and implementation of complex software systems. When you’re writing code, there are thousands of lines in an application, and it’s difficult to keep track of the relationships and hierarchies within a software system. UML diagrams divide that software system into components and subcomponents."

class Question_5(Chapter_4):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.question = "A part of mathematical science that deals with sets, or groups of things, and is used as the basis for data manipulation in the relational model?"
        self.solution = "Set Theory"
        self.description = "A part of mathematical science that deals with sets, or groups of things, and is used as the basis for data manipulation in the relational model."

class Question_6(Chapter_4):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.question = "What can refer to a visual representation of a database, a set of rules that govern a database, or to the entire set of objects belonging to a particular user?"
        self.solution = "Schema"
        self.description = "A database schema represents the logical configuration of all or part of a relational database. It can exist both as a visual representation and as a set of formulas known as integrity constraints that govern a database. These formulas are expressed in a data definition language, such as SQL. As part of a data dictionary, a database schema indicates how the entities that make up the database relate to one another, including tables, views, stored procedures, and more."

class Question_7(Chapter_4):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.question = "What is an attribute whose value is calculated (derived) from other attributes?"
        self.solution = "Derived Attribute"
        self.description = "An attribute that does not physically exist within the entity and is derived via an algorithm. For example, the Age attribute might be derived by subtracting the birth date from the current date."

class Question_8(Chapter_4):

    def __init__(self):
        super().__init__()
        self.numQ = 8
        self.question = "What is not dependent on any other entity in the schema?"
        self.solution = "Strong Entity"
        self.description = "A strong entity is not dependent on any other entity in the schema. A strong entity will always have a primary key.\nStrong entities are represented by a single rectangle. The relationship of two strong entities is represented by a single diamond.\nVarious strong entities, when combined together, create a strong entity set. "

class Question_9(Chapter_4):

    def __init__(self):
        super().__init__()
        self.numQ = 9
        self.question = "What is dependent on a strong entity to ensure its existence?"
        self.solution = "Weak Entity"
        self.description = "A weak entity is dependent on a strong entity to ensure its existence. Unlike a strong entity, a weak entity does not have any primary key. It instead has a partial discriminator key.\n A weak entity is represented by a double rectangle. The relation between one strong and one weak entity is represented by a double diamond. This relationship is also known as identifying relationship."
#
# class Question_10(Chapter_4):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 10
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_11(Chapter_4):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 11
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_12(Chapter_4):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 12
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_13(Chapter_4):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 13
#         self.question = ""
#         self.solution = ""
#         self.description = ""
