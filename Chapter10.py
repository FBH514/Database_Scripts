from Template import Template
from random import shuffle

# –––––––––––––––––––––––––Chapter 10–––––––––––––––––––––––––

class Chapter_10(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13

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
        q12 = Question_12()
        q13 = Question_13()

        question_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13]
        shuffle(question_list)
        return question_list

class Question_1(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "What do you call a sequence of database operations that access the database?"
        self.solution = "Transaction"
        self.description = "A transaction is a sequence of database operations that access the database. A trans- action is a logical unit of work; that is, all parts are executed or the transaction is aborted. A transaction takes a database from one consistent state to another. A consistent database state is one in which all data integrity constraints are satisfied."

class Question_2(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "Name one of the four properties are sometimes referred to as the ACID test."
        self.solution = ["Atomicity", "Consistency", "Isolation", "Durability"]
        self.description = "Each individual transaction must display atomicity, consistency, isolation, and durability. These four properties are sometimes referred to as the ACID test."

class Question_3(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "Which transaction property that requires all parts of a transaction to be treated as a single, indivisible, logical unit of work?"
        self.solution = "Atomicity"
        self.description = "Atomicity is a transaction property that requires all parts of a transaction to be treated as a single, indivisible, logical unit of work? All parts of a transaction must be completed or the entire transaction is aborted."

class Question_4(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "What means that the database’s consistent state is maintained?"
        self.solution = "Consistency"
        self.description = "Consistency means that the database’s consistent state is maintained. Isolation means that data used by one transaction cannot be accessed by another transaction until the first one is completed. "

class Question_5(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "What means that data used by one transaction cannot be accessed by another transaction until the first one is completed?"
        self.solution = "Isolation"
        self.description = "Isolation means that data used by one transaction cannot be accessed by another transaction until the first one is completed."

class Question_6(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "What means that changes made by a transaction cannot be rolled back once the transaction is committed?"
        self.solution = "Durability"
        self.description = "Durability means that changes made by a transaction cannot be rolled back once the transaction is committed."

class Question_7(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "What control coordinates the simultaneous execution of transactions?"
        self.solution = "Concurrency"
        self.description = "Concurrency control coordinates the simultaneous execution of transactions. The concurrent execution of transactions can result in three main problems: lost updates, uncommitted data, and inconsistent retrievals."

class Question_8(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 8
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "What is responsible for establishing the order in which the concurrent transaction operations are executed?"
        self.solution = "Scheduler"
        self.description = "The scheduler is responsible for establishing the order in which the concurrent transaction operations are executed. The transaction execution order is critical and ensures database integrity in multiuser database systems. The scheduler uses locking, time stamping, and optimistic methods to ensure the serializability of transactions."

class Question_9(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 9
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "What guarantees unique access to a data item by a transaction?"
        self.solution = "Locks"
        self.description = "A lock guarantees unique access to a data item by a transaction. The lock prevents one transaction from using the data item while another transaction is using it. There are several levels of locks: database, table, page, row, and field. Two types of locks can be used in database systems: binary locks and shared/exclusive locks."

class Question_10(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 10
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "Which lock type can have only two states: locked (1) or unlocked (0) ?"
        self.solution = "Binary Lock"
        self.description = "A binary lock can have only two states: locked (1) or unlocked (0)."

class Question_11(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 11
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "What is used when a transaction wants to read data from a database and no other transaction is updating the same data?"
        self.solution = "Shared Lock"
        self.description = "A shared lock is used when a transaction wants to read data from a database and no other transaction is updating the same data. Several shared or “read” locks can exist for a particular item. An exclusive lock is issued when a transaction wants to update (write to) the database and no other locks (shared or exclusive) are held on the data."

class Question_12(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 12
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "What is guaranteed through the use of two-phase locking?"
        self.solution = "Serializability"
        self.description = "Serializability of schedules is guaranteed through the use of two-phase locking. The two-phase locking schema has a growing phase, in which the transaction acquires all of the locks that it needs without unlocking any data, and a shrinking phase, in which the transaction releases all of the locks without acquiring new locks. When two or more transactions wait indefinitely for each other to release a lock, they are in a deadlock, also called a deadly embrace. There are three deadlock control techniques: prevention, detection, and avoidance."

class Question_13(Chapter_10):

    def __init__(self):
        super().__init__()
        self.numQ = 13
        self.chapter = 10
        self.chapter_name = "Transaction Management and Concurrency Control"
        self.numQuestions = 13
        self.question = "What restores the database from a given state to a previous consistent state?"
        self.solution = "Database recovery"
        self.description = "Database recovery restores the database from a given state to a previous consistent state. Database recovery is triggered when a critical event occurs, such as a hardware error or application error."

# class Question_14(Chapter_10):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 14
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_15(Chapter_10):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 15
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_16(Chapter_10):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 16
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_17(Chapter_10):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 17
#         self.question = ""
#         self.solution = ""
#         self.description = ""
