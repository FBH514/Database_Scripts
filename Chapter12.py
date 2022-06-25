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

    # def main(self):
    #     count = 0
    #     for item in self.return_questions():
    #         print()
    #         print(f"Question {item.numQ}, chapter {self.chapter}\n{item.question}")
    #         self.beautify(15)
    #         answer = input("Enter your answer ––> ")
    #
    #         if answer.casefold() in item.solution.casefold():
    #             count += 1
    #             self.grade(count)
    #             print(self.compliments())
    #         else:
    #             print(self.invalid_answer())
    #
    #         print(f"Solution to Question {item.numQ}, chapter {self.chapter} ––> {item.solution} ")
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


class Question_1(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.question = "What stores logically related data in two or more physically independent sites connected via a computer network?"
        self.solution = "Distributed Database"
        self.description = "A distributed database stores logically related data in two or more physically independent sites connected via a computer network. The database is divided into fragments, which can be a horizontal set of rows or a vertical set of attributes. Each fragment can be allocated to a different network node."

class Question_2(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.question = "What is the division of logical database processing among two or more network nodes?"
        self.solution = "Distributed processing"
        self.description = "Distributed processing is the division of logical database processing among two or more network nodes. Distributed databases require distributed processing. A distributed database management system (DDBMS) governs the processing and storage of logically related data through interconnected computer systems."

class Question_3(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.question = "What do you call the resident software on each computer node that requests data?"
        self.solution = "transaction processor"
        self.description = "The main components of a DDBMS are the transaction processor (TP) and the data processor (DP). The transaction processor component is the resident software on each computer node that requests data. The data processor component is the resident software on each computer that stores and retrieves data."

class Question_4(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.question = "What do you call the resident software on each computer that stores and retrieves data?"
        self.solution = "data processor"
        self.description = "The main components of a DDBMS are the transaction processor (TP) and the data processor (DP). The transaction processor component is the resident software on each computer node that requests data. The data processor component is the resident software on each computer that stores and retrieves data."

class Question_5(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.question = "What shares the common objective of making the distributed database behave as though it were a centralized database system?"
        self.solution = "transparencies"
        self.description = "DDBMS characteristics are best described as a set of transparencies: distribution, transaction, performance, failure, and heterogeneity. All transparencies share the common objective of making the distributed database behave as though it were a centralized database system; that is, the end user sees the data as part of a single, logical centralized database and is unaware of the system’s complexities."

class Question_6(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.question = "What is formed by one or more database requests?"
        self.solution = "transaction"
        self.description = "A transaction is formed by one or more database requests. An undistributed transaction updates or requests data from a single site. A distributed transaction can update or request data from multiple sites."

class Question_7(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.question = "What's required in a network of distributed databases?"
        self.solution = "Distributed concurrency control"
        self.description = "Distributed concurrency control is required in a network of distributed databases. A two- phase COMMIT protocol is used to ensure that all parts of a transaction are completed"

class Question_8(Chapter_12):

    def __init__(self):
        super().__init__()
        self.numQ = 8
        self.question = "What are designed to determine the location of the database fragments or replicas?"
        self.solution = "Data allocation strategies"
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
