from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 8–––––––––––––––––––––––––

class Chapter_8(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 8
        self.chapter_name = "Advanced SQL"
        self.numQuestions = 10

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
        q10 = Question_10()

        question_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
        shuffle(question_list)
        return question_list

class Question_1(Chapter_8):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 8
        self.chapter_name = "Advanced SQL"
        self.numQuestions = 10
        self.question = "Which command is used to add new rows to tables?"
        self.solution = "INSERT"
        self.description = "The INSERT command is used to add new rows to tables."

class Question_2(Chapter_8):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 8
        self.chapter_name = "Advanced SQL"
        self.numQuestions = 10
        self.question = "Which command is used to modify data values in existing rows of a table?"
        self.solution = "UPDATE"
        self.description = "The UPDATE command is used to modify data values in existing rows of a table."

class Question_3(Chapter_8):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 8
        self.chapter_name = "Advanced SQL"
        self.numQuestions = 10
        self.question = "Which command is used to delete rows from tables?"
        self.solution = "DELETE"
        self.description = "The DELETE command is used to delete rows from tables."

class Question_4(Chapter_8):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 8
        self.chapter_name = "Advanced SQL"
        self.numQuestions = 10
        self.question = "Which command is used to roll back changes made to the rows and is Phase 1 of the 2PC?"
        self.solution = "ROLLBACK"
        self.description = "The COMMIT and ROLLBACK commands are used to permanently save or roll back changes made to the rows."

class Question_5(Chapter_8):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.chapter = 8
        self.chapter_name = "Advanced SQL"
        self.numQuestions = 10
        self.question = "Which command is used to commit changes made to the rows and is Phase 2 of the 2PC?"
        self.solution = "COMMIT"
        self.description = "The COMMIT and ROLLBACK commands are used to permanently save or roll back changes made to the rows."

class Question_6(Chapter_8):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.chapter = 8
        self.chapter_name = "Advanced SQL"
        self.numQuestions = 10
        self.question = "What can be created to expose subsets of data to end users primarily for security and privacy reasons?"
        self.solution = "Views"
        self.description = "Views can be created to expose subsets of data to end users primarily for security and privacy reasons. Normally, views only store the SELECT statement to produce the view. Materialized views store a separate copy of the data and must be refreshed regularly."

class Question_7(Chapter_8):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.chapter = 8
        self.chapter_name = "Advanced SQL"
        self.numQuestions = 10
        self.question = "What may be used to generate values to be assigned to a record?"
        self.solution = "Sequences"
        self.description = "In Oracle and SQL Server, sequences may be used to generate values to be assigned to a record. For example, a sequence may be used to number invoices automatically. MS Access uses an AutoNumber data type to generate numeric sequences, and MySQL uses the AUTO_INCREMENT property during table creation. Oracle and SQL Server can use the Identity column property to designate the column that will have sequential numeric values automatically assigned to it. There can only be one Identity column per table."

class Question_8(Chapter_8):

    def __init__(self):
        super().__init__()
        self.numQ = 8
        self.chapter = 8
        self.chapter_name = "Advanced SQL"
        self.numQuestions = 10
        self.question = "What is procedural SQL code that is automatically invoked by the DBMS upon the occurrence of a specified data manipulation event (UPDATE, INSERT, or DELETE) ?"
        self.solution = "Triggers"
        self.description = "A trigger is procedural SQL code that is automatically invoked by the DBMS upon the occurrence of a specified data manipulation event (UPDATE, INSERT, or DELETE). Triggers are critical to proper database operation and management. They help automate various transaction and data management processes, and they can be used to enforce constraints that are not enforced at the DBMS design and implementation levels."

class Question_9(Chapter_8):

    def __init__(self):
        super().__init__()
        self.numQ = 9
        self.chapter = 8
        self.chapter_name = "Advanced SQL"
        self.numQuestions = 10
        self.question = "What is a named collection of SQL statements?"
        self.solution = "Stored Procedure"
        self.description = "Just like database triggers, stored procedures are stored in the database. One of the major advantages of stored procedures is that they can be used to encapsulate and represent complete business trans- actions. Use of stored procedures substantially reduces network traffic and increases system performance."

class Question_10(Chapter_8):

    def __init__(self):
        super().__init__()
        self.numQ = 10
        self.chapter = 8
        self.chapter_name = "Advanced SQL"
        self.numQuestions = 10
        self.question = "What refers to the use of SQL statements within an application program- ming language such as Visual Basic .NET, C#, COBOL, or Java?"
        self.solution = "Embedded SQL"
        self.description = "Embedded SQL refers to the use of SQL statements within an application program- ming language such as Visual Basic .NET, C#, COBOL, or Java. The language in which the SQL statements are embedded is called the host language. Embedded SQL is still the most common approach to maintaining procedural capabilities in DBMS- based applications."

# class Question_12(Chapter_8):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 12
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_13(Chapter_8):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 13
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_14(Chapter_8):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 14
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_15(Chapter_8):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 15
#         self.question = ""
#         self.solution = ""
#         self.description = ""
