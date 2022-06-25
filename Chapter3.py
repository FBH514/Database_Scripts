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

    # def main(self):
    #     count = 0
    #     for item in self.return_questions():
    #         print()
    #         print(f"Question {item.numQ}, chapter {self.chapter}\n{item.question}")
    #         self.beautify(15)
    #         answer = input("Enter your answer ––> ")
    #         print(f"Solution to Question {item.numQ}, chapter {self.chapter} ––> {item.solution} ")
    #
    #         if answer in item.solution.casefold():
    #             count += 1
    #             self.grade(count)
    #             print(self.compliments())
    #         else:
    #             print(self.invalid_answer())
    #         self.beautify(15)
    #         print(f"More info about {item.solution}\n{item.description}")
    #         self.beautify(25)
    #         print()
    #
    #         correction = input("Do you need to manually correct your answer? Y/N ––>")
    #
    #         if correction == "Y".casefold() or correction == "Yes".casefold():
    #             print(self.compliments())
    #             self.grade(count)
    #         else:
    #             continue
    #
    #     print()
    #     self.beautify(5)
    #     print(f"You scored {count}/{self.numQuestions} ––> {self.grade(count)}")
    #     self.beautify(35)

class Question_1(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.question = "What are the basic building blocks of a relational database?"
        self.solution = "Tables"
        self.description = "Tables are the basic building blocks of a relational database. A grouping of related entities, known as an entity set, is stored in a table. Conceptually speaking, the relational table is composed of intersecting rows (tuples) and columns. Each row represents a single entity, and each column represents the characteristics (attributes) of the entities"

class Question_2(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.question = "What defines functional dependencies?"
        self.solution = "Keys"
        self.description = "Keys are central to the use of relational databases. Keys define functional dependencies; that is, other attributes are dependent on the key and can therefore be found if the key value is known. A key can be classified as a super key, a candidate key, a primary key, a secondary key, or a foreign key"

class Question_3(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.question = "What is an attribute or a combination of attributes that uniquely identifies all remaining attributes found in any given row?"
        self.solution = "Primary Keys"
        self.description = "Each table row must have a primary key. The primary key is an attribute or combination of attributes that uniquely identifies all remaining attributes found in any given row. Because a primary key must be unique, no null values are allowed if entity integrity is to be maintained."

class Question_4(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.question = "What dictates that the foreign key must contain values that match the primary key in the related table or must contain nulls?"
        self.solution = "Referential Integrity"
        self.description = "Although tables are independent, they can be linked by common attributes. Thus, the primary key of one table can appear as the foreign key in another table to which it is linked. Referential Integrity dictates that the foreign key must contain values that match the primary key in the related table or must contain nulls."

class Question_5(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.question = "What automatically produces a structure to house a data dictionary for your database?"
        self.solution = "RDBMS"
        self.description = "A relational database performs much of the data manipulation work behind the scenes. For example, when you create a database, the RDBMS automatically produces a structure to house a data dictionary for your database. Each time you create a new table within the database, the RDBMS updates the data dictionary, thereby providing the database documentation."

class Question_6(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.question = "What is a constraint that determines the relation of one attribute to another attribute in a Database Management System (DBMS)?"
        self.solution = "Functional Dependency"
        self.description = "Functional Dependency (FD) is a constraint that determines the relation of one attribute to another attribute in a Database Management System (DBMS). Functional Dependency helps to maintain the quality of data in the database. It plays a vital role to find the difference between good and bad database design."

class Question_7(Chapter_3):

    def __init__(self):
        super().__init__()
        self.numQ = 7
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
