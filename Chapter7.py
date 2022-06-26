from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 7–––––––––––––––––––––––––

class Chapter_7(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11

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
        q11 = Question_11()

        question_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11]
        shuffle(question_list)
        return question_list

class Question_1(Chapter_7):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11
        self.question = "What can be divided into two overall categories: data definition language (DDL) commands and data manipulation language (DML) commands?"
        self.solution = "SQL Commands"
        self.description = "Data Definition Language (DDL) and Data Manipulation Language (DML) together forms a Database Language. The basic difference between DDL and DML is that DDL (Data Definition Language) is used to Specify the database schema database structure.\n\nOn the other hand, DML (Data Manipulation Language) is used to access, modify or retrieve the data from the database."

class Question_2(Chapter_7):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11
        self.solution = ["NUMBER", "NUMERIC", "INTEGER", "CHAR", "VARCHAR", "DATE"]
        self.question = "Name one of the {} ANSI standard data types.".format(len(self.solution))

class Question_3(Chapter_7):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11
        self.question = "What is the main data retrieval command in SQL?"
        self.solution = "SELECT"
        self.description = "The SELECT statement is the most commonly used command in Structured Query Language. It is used to access the records from one or more database tables and views. It also retrieves the selected data that follow the conditions we want."

class Question_4(Chapter_7):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11
        self.question = "What is the traditional join in which only rows that meet a given criterion are selected?"
        self.solution = "Inner Join"
        self.description = ""


class Question_5(Chapter_7):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11
        self.question = "What returns the matching rows as well as the rows with unmatched attribute values for one table or both tables to be joined?"
        self.solution = "Outer Join"
        self.description = ""

class Question_6(Chapter_7):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11
        self.question = "Name returns all rows with matching values in the matching columns and eliminates duplicate columns."
        self.solution = "Natural Join"
        self.description = "A natural join returns all rows with matching values in the matching columns and eliminates duplicate columns. This style of query is used when the tables share a common attribute with a common name."

class Question_7(Chapter_7):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11
        self.question = "What is used to sort the output of a SELECT statement?"
        self.solution = "ORDER BY"
        self.description = "The ORDER BY clause is used to sort the output of a SELECT statement. The ORDER BY clause can sort by one or more columns and can use either ascending or descending order."

class Question_8(Chapter_7):

    def __init__(self):
        super().__init__()
        self.numQ = 8
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11
        self.question = "What can be used with the SELECT, UPDATE, and DELETE statements to restrict the rows affected by the DDL command?"
        self.solution = "WHERE"
        self.description = "The WHERE clause can be used with the SELECT, UPDATE, and DELETE statements to restrict the rows affected by the DDL command. The condition list represents one or more conditional expressions separated by logical operators (AND, OR, and NOT). The conditional expression can contain any comparison operators (=, >, <, >=, <=, and <>) as well as special operators (BETWEEN, IS NULL, LIKE, IN, and EXISTS)."

class Question_9(Chapter_7):

    def __init__(self):
        super().__init__()
        self.numQ = 9
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11
        self.question = "Name what are usually used in conjunction with the GROUP BY clause to group the output of aggregate computations by one or more attributes."
        self.solution = "Aggregate Functions"
        self.description = "Aggregate functions (COUNT, MIN, MAX, and AVG) are special functions that per- form arithmetic computations over a set of rows. The aggregate functions are usually used in conjunction with the GROUP BY clause to group the output of aggregate computations by one or more attributes. The HAVING clause is used to restrict the output of the GROUP BY clause by selecting only the aggregate rows that match a given condition."

class Question_10(Chapter_7):

    def __init__(self):
        super().__init__()
        self.numQ = 10
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11
        self.question = "What are used when it is necessary to process data based on other processed data?"
        self.solution = "Subqueries / Correlated"
        self.description = "Subqueries and correlated queries are used when it is necessary to process data based on other processed data. That is, the query uses results that were previously unknown and that are generated by another query. Subqueries may be used with the FROM, WHERE, IN, and HAVING clauses in a SELECT statement. A subquery may return a single row or multiple rows."

class Question_11(Chapter_7):

    def __init__(self):
        super().__init__()
        self.numQ = 11
        self.chapter = 7
        self.chapter_name = "Introduction to SQL"
        self.numQuestions = 11
        self.question = "Which set operator combines the output of two or more queries and produce a new relation with all unique rows from both queries?"
        self.solution = "UNION"
        self.description = "SQL provides relational set operators to combine the output of two queries to generate a new relation. The UNION and UNION ALL set operators combine the output of two or more queries and produce a new relation with all unique (UNION) or duplicate (UNION ALL) rows from both queries. The INTERSECT relational set operator selects only the common rows. The EXCEPT (MINUS) set operator selects only the rows that are different. UNION, INTERSECT, and EXCEPT require union-compatible relations."

# class Question_12(Chapter_7):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 12
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_13(Chapter_7):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 13
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_14(Chapter_7):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 14
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_15(Chapter_7):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 15
#         self.question = ""
#         self.solution = ""
#         self.description = ""
