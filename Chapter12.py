# question 2 solution to fix


from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 12–––––––––––––––––––––––––

class Chapter_12(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 12
        self.chapter_name = "Distributed Database Management Systems"
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

class Question_1(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 12
        self.chapter_name = "Distributed Database Management Systems"
        self.numQuestions = 8
        self.question = "What stores logically related data in two or more physically independent sites connected via a computer network?"
        self.solution = "Distributed Database"
        self.description = "A distributed database stores logically related data in two or more physically independent sites connected via a computer network. The database is divided into fragments, which can be a horizontal set of rows or a vertical set of attributes. Each fragment can be allocated to a different network node."

class Question_2(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 12
        self.chapter_name = "Distributed Database Management Systems"
        self.numQuestions = 8
        self.question = "What is the division of logical database processing among two or more network nodes?"
        self.solution = "Distributed Processing"
        self.description = "Distributed processing is the division of logical database processing among two or more network nodes. Distributed databases require distributed processing. A distributed database management system (DDBMS) governs the processing and storage of logically related data through interconnected computer systems."

class Question_3(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 12
        self.chapter_name = "Distributed Database Management Systems"
        self.numQuestions = 8
        self.question = "What do you call the resident software on each computer node that requests data?"
        self.solution = "Transaction Processor"
        self.description = "The main components of a DDBMS are the transaction processor (TP) and the data processor (DP). The transaction processor component is the resident software on each computer node that requests data. The data processor component is the resident software on each computer that stores and retrieves data."

class Question_4(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 12
        self.chapter_name = "Distributed Database Management Systems"
        self.numQuestions = 8
        self.question = "What do you call the resident software on each computer that stores and retrieves data?"
        self.solution = "Data Processor"
        self.description = "The main components of a DDBMS are the transaction processor (TP) and the data processor (DP). The transaction processor component is the resident software on each computer node that requests data. The data processor component is the resident software on each computer that stores and retrieves data."

class Question_5(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.chapter = 12
        self.chapter_name = "Distributed Database Management Systems"
        self.numQuestions = 8
        self.question = "What shares the common objective of making the distributed database behave as though it were a centralized database system?"
        self.solution = "Transparencies"
        self.description = "DDBMS characteristics are best described as a set of transparencies: distribution, transaction, performance, failure, and heterogeneity. All transparencies share the common objective of making the distributed database behave as though it were a centralized database system; that is, the end user sees the data as part of a single, logical centralized database and is unaware of the system’s complexities."

class Question_6(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.chapter = 12
        self.chapter_name = "Distributed Database Management Systems"
        self.numQuestions = 8
        self.question = "What is formed by one or more database requests?"
        self.solution = "Transaction"
        self.description = "A transaction is formed by one or more database requests. An undistributed transaction updates or requests data from a single site. A distributed transaction can update or request data from multiple sites."

class Question_7(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.chapter = 12
        self.chapter_name = "Distributed Database Management Systems"
        self.numQuestions = 8
        self.question = "What's required in a network of distributed databases?"
        self.solution = "Distributed Concurrency Control"
        self.description = "Distributed concurrency control is required in a network of distributed databases. A two- phase COMMIT protocol is used to ensure that all parts of a transaction are completed"

class Question_8(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 8
        self.chapter = 12
        self.chapter_name = "Distributed Database Management Systems"
        self.numQuestions = 8
        self.question = "What are designed to determine the location of the database fragments or replicas?"
        self.solution = "Data Allocation Strategies"
        self.description = "A database can be replicated over several different sites on a computer network. The replication of the database fragments has the objective of improving data availability, thus decreasing access time. A database can be partially, fully, or not replicated. Data allocation strategies are designed to determine the location of the database fragments or replicas."

# class Question_9(Chapter_12):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 9
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_10(Chapter_12):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 10
#         self.question = ""
#         self.solution = ""
#         self.description = ""
