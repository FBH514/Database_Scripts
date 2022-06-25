from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 3–––––––––––––––––––––––––

class Chapter_3(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 3
        self.chapter_name = "Relational Database Model"
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

class Question_1(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 3
        self.chapter_name = "Relational Database Model"
        self.numQuestions = 7
        self.question = "What are the basic building blocks of a relational database?"
        self.solution = "Tables"
        self.description = "Tables are the basic building blocks of a relational database. A grouping of related entities, known as an entity set, is stored in a table. Conceptually speaking, the relational table is composed of intersecting rows (tuples) and columns. Each row represents a single entity, and each column represents the characteristics (attributes) of the entities"

class Question_2(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 3
        self.chapter_name = "Relational Database Model"
        self.numQuestions = 7
        self.question = "What defines functional dependencies?"
        self.solution = "Keys"
        self.description = "Keys are central to the use of relational databases. Keys define functional dependencies; that is, other attributes are dependent on the key and can therefore be found if the key value is known. A key can be classified as a super key, a candidate key, a primary key, a secondary key, or a foreign key"

class Question_3(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 3
        self.chapter_name = "Relational Database Model"
        self.numQuestions = 7
        self.question = "What is an attribute or a combination of attributes that uniquely identifies all remaining attributes found in any given row?"
        self.solution = "Primary Keys"
        self.description = "Each table row must have a primary key. The primary key is an attribute or combination of attributes that uniquely identifies all remaining attributes found in any given row. Because a primary key must be unique, no null values are allowed if entity integrity is to be maintained."

class Question_4(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 3
        self.chapter_name = "Relational Database Model"
        self.numQuestions = 7
        self.question = "What dictates that the foreign key must contain values that match the primary key in the related table or must contain nulls?"
        self.solution = "Referential Integrity"
        self.description = "Although tables are independent, they can be linked by common attributes. Thus, the primary key of one table can appear as the foreign key in another table to which it is linked. Referential Integrity dictates that the foreign key must contain values that match the primary key in the related table or must contain nulls."

class Question_5(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.chapter = 3
        self.chapter_name = "Relational Database Model"
        self.numQuestions = 7
        self.question = "What automatically produces a structure to house a data dictionary for your database?"
        self.solution = "RDBMS"
        self.description = "A relational database performs much of the data manipulation work behind the scenes. For example, when you create a database, the RDBMS automatically produces a structure to house a data dictionary for your database. Each time you create a new table within the database, the RDBMS updates the data dictionary, thereby providing the database documentation."

class Question_6(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.chapter = 3
        self.chapter_name = "Relational Database Model"
        self.numQuestions = 7
        self.question = "What is a constraint that determines the relation of one attribute to another attribute in a Database Management System (DBMS)?"
        self.solution = "Functional Dependency"
        self.description = "Functional Dependency (FD) is a constraint that determines the relation of one attribute to another attribute in a Database Management System (DBMS). Functional Dependency helps to maintain the quality of data in the database. It plays a vital role to find the difference between good and bad database design."

class Question_7(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.chapter = 3
        self.chapter_name = "Relational Database Model"
        self.numQuestions = 7
        self.question = "What are generally used to speed up and facilitate data retrieval?"
        self.solution = "Indexes"
        self.description = "An ordered array of index key values and row ID values (pointers). Indexes are generally used to speed up and facilitate data retrieval. Also known as an index key."

# class Question_8(Chapter_3):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 8
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_9(Chapter_3):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 9
#         self.question = ""
#         self.solution = ""
#         self.description = ""

# class Question_10(Chapter_3):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 10
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_11(Chapter_3):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 11
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_12(Chapter_3):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 12
#         self.question = ""
#         self.solution = ""
#         self.description = ""
