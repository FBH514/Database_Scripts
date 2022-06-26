from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 11–––––––––––––––––––––––––

class Chapter_11(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 11
        self.chapter_name = "Database Performance Tuning and Query Optimization"
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

class Question_1(Chapter_11):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 11
        self.chapter_name = "Database Performance Tuning and Query Optimization"
        self.numQuestions = 9
        self.question = "What refers to a set of activities and procedures designed to ensure that an end-user query is processed by the DBMS in the least amount of time?"
        self.solution = "Database performance tuning"
        self.description = "Database performance tuning refers to a set of activities and procedures designed to ensure that an end-user query is processed by the DBMS in the least amount of time. SQL performance tuning refers to activities on the client side that are designed to generate SQL code that returns the correct answer in the least amount of time, using the minimum amount of resources at the server end. DBMS performance tuning refers to activities on the server side that are oriented so the DBMS is properly configured to respond to clients’ requests in the fastest way possible while making optimum use of existing resources."

class Question_2(Chapter_11):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 11
        self.chapter_name = "Database Performance Tuning and Query Optimization"
        self.numQuestions = 9
        self.question = "What refers to a number of measurements gathered by the DBMS that describe a snapshot of the database objects’ characteristics?"
        self.solution = "Database statistics"
        self.description = "Database statistics refer to a number of measurements gathered by the DBMS that describe a snapshot of the database objects’ characteristics. The DBMS gathers statistics about objects such as tables, indexes, and available resources, which include the number of processors used, processor speed, and temporary space available. The DBMS uses the statistics to make critical decisions about improving query processing efficiency."

class Question_3(Chapter_11):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 11
        self.chapter_name = "Database Performance Tuning and Query Optimization"
        self.numQuestions = 9
        self.question = "What are crucial in the process that speeds up data access?"
        self.solution = "Indexes"
        self.description = "Indexes are crucial in the process that speeds up data access. Indexes facilitate searching, sorting, and using aggregate functions and join operations. The improvement in data access speed occurs because an index is an ordered set of values that contains the index key and pointers. Data sparsity refers to the number of different values a column could have. Indexes are recommended in high-sparsity columns used in search conditions."

class Question_4(Chapter_11):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 11
        self.chapter_name = "Database Performance Tuning and Query Optimization"
        self.numQuestions = 9
        self.question = "When does the DBMS must choose what indexes to use, how to perform join operations, which table to use first, and so on?"
        self.solution = "Query Optimization"
        self.description = "During query optimization, the DBMS must choose what indexes to use, how to perform join operations, which table to use first, and so on. Each DBMS has its own algorithms for determining the most efficient way to access the data. The two most common approaches are rule-based and cost-based optimization."

class Question_5(Chapter_11):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.chapter = 11
        self.chapter_name = "Database Performance Tuning and Query Optimization"
        self.numQuestions = 9
        self.question = "What uses preset rules and points to determine the best approach to execute a query?"
        self.solution = "rule-based optimizer"
        self.description = "A rule-based optimizer uses preset rules and points to determine the best approach to execute a query. A cost-based optimizer uses sophisticated algorithms based on statistics about the objects being accessed to determine the best approach to execute a query. In this case, the optimizer process adds up the processing cost, the I/O costs, and the resource costs (RAM and temporary space) to determine the total cost of a given execution plan."

class Question_6(Chapter_11):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.chapter = 11
        self.chapter_name = "Database Performance Tuning and Query Optimization"
        self.numQuestions = 9
        self.question = "What deals with writing queries that make good use of the statistics?"
        self.solution = "SQL performance tuning"
        self.description = "SQL performance tuning deals with writing queries that make good use of the statistics. In particular, queries should make good use of indexes. Indexes are very useful when you want to select a small subset of rows from a large table based on a condition."

class Question_7(Chapter_11):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.chapter = 11
        self.chapter_name = "Database Performance Tuning and Query Optimization"
        self.numQuestions = 9
        self.question = ""
        self.solution = ""
        self.description = ""

class Question_8(Chapter_11):

    def __init__(self):
        super().__init__()
        self.numQ = 8
        self.chapter = 11
        self.chapter_name = "Database Performance Tuning and Query Optimization"
        self.numQuestions = 9
        self.question = "What deals with how to translate business questions into specific SQL code to generate the required results?"
        self.solution = "Query formulation"
        self.description = "Query formulation deals with how to translate business questions into specific SQL code to generate the required results. To do this, you must carefully evaluate which columns, tables, and computations are required to generate the desired output."

class Question_9(Chapter_11):

    def __init__(self):
        super().__init__()
        self.numQ = 9
        self.chapter = 11
        self.chapter_name = "Database Performance Tuning and Query Optimization"
        self.numQuestions = 9
        self.question = "What includes tasks such as managing the DBMS processes in primary memory (allocating memory for caching purposes) and managing the structures in physical storage (allocating space for the data files)?"
        self.solution = "DBMS performance tuning"
        self.description = "DBMS performance tuning includes tasks such as managing the DBMS processes in primary memory (allocating memory for caching purposes) and managing the structures in physical storage (allocating space for the data files)."
#
# class Question_10(Chapter_11):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 10
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
#
# class Question_11(Chapter_11):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 11
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
#
# class Question_12(Chapter_11):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 12
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
#
# class Question_13(Chapter_11):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 13
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
