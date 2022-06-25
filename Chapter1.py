from Template import Template
from random import shuffle

# –––––––––––––––––––––––––Chapter 1–––––––––––––––––––––––––

class Chapter_1(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 1
        self.chapter_name = "Database Systems"
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

    # def main(self):
    #     count = 0
    #     for item in self.return_questions():
    #         print()
    #         print(f"Chapter {self.chapter} | {self.chapter_name}\nQuestion {item.numQ}\n{item.question}")
    #         self.beautify(15)
    #         answer = input("Enter your answer ––> ")
    #         print(f"Solution to Chapter {self.chapter}, Question {item.numQ} ––> {item.solution} ")
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
    #         correction = input("Do you need to manually correct your answer? Y/N ––> ")
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
    #

class Question_1(Chapter_1):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.question = "What consists of raw facts?"
        self.solution = "Data"
        self.description = "Data consists of raw facts. Information is the result of processing data to reveal its meaning. Accurate, relevant, and timely information is the key to good decision marking, and good decision making is the key to organizational survival in a global environment."

class Question_2(Chapter_1):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.question = "Name the operating system you need to implement a database and manage its contents?"
        self.solution = "DBMS"
        self.description = "Data is usually stored in a database. To implement a database and to manage its contents, you need a database management system (DBMS). The DBMS servers as the intermediary between the user and the database. The database contains the data you have collected and \"data about data\", known as metadata."

class Question_3(Chapter_1):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.question = "What defines the database structure?"
        self.solution = "Database Design"
        self.description = "Database design defines the database structure. A well-designed database facilitates data management and generates accurate and valuable information. A poorly designed database can lead to poor decision making, and poor decision making can lead to the failure of an organization."

class Question_4(Chapter_1):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.question = "What provides information about each attribute, also referred to as fields, of a data model?"
        self.solution = "Data Dictionary"
        self.description = "A Data Dictionary provides information about each attribute, also referred to as fields, of a data model. An attribute is a place in the database that holds information.\n\nA Data Dictionary is typically organized in a spreadsheet format. Each attribute is listed as a row in the spreadsheet and each column labels an element of information that is useful to know about the attribute."

class Question_5(Chapter_1):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.question = "What defines the characteristics or the properties of an entity?"
        self.solution = "Attributes"
        self.description = "A Data Dictionary provides information about each attribute, also referred to as fields, of a data model. An attribute is a place in the database that holds information.\n\nA Data Dictionary is typically organized in a spreadsheet format. Each attribute is listed as a row in the spreadsheet and each column labels an element of information that is useful to know about the attribute."

class Question_6(Chapter_1):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.question = "What is the result of processing raw data to reveal its meaning?"
        self.solution = "Information"
        self.description = "Information is the result of processing raw data to reveal its meaning. Data processing can be as simple as organizing data to reveal patterns or as complex as making forecasts or drawing inferences using statistical modeling. To reveal meaning, information requires context."

class Question_7(Chapter_1):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.question = "What is the term used to define data about data?"
        self.solution = "Metadata"
        self.description = "The metadata describes the data characteristics and the set of relationships that links the data found within the database. For example, the metadata component stores information such as the name of each data element, the type of values (numeric, dates, or text) stored on each data element, and whether the data element can be left empty. The metadata provides information that complements and expands the value and use of the data. In short, metadata presents a more complete picture of the data in the database. Given the characteristics of metadata, you might hear a database described as a \"collection of self-describing data\"."

class Question_8(Chapter_1):

    def __init__(self):
        super().__init__()
        self.numQ = 8
        self.question = "What is the ability to make changes in the structure of the database without affecting the user’s ability to operate the data?"
        self.solution = "Structural Independence"
        self.description = "Structural independence exists when changes in the database structure do not affect DBMS ability to access data."

class Question_9(Chapter_1):

    def __init__(self):
        super().__init__()
        self.numQ = 9
        self.question = "What exists when the same data is stored unnecessarily at different places?"
        self.solution = "Redundancy"
        self.description = "Uncontrolled data redundancy sets the stage for the following:\n• Poor data security. Having multiple copies of data increases the chances for a copy of the data to be susceptible to unauthorized access.\n• Data inconsistency. Data inconsistency exists when different and conflicting versions of the same data appear in different places\n• Data-entry errors. Data-entry errors are more likely to occur when complex entries (such as 10-digit phone numbers) are made in several different files or recur frequently in one or more files.\n• Data integrity problems. It is possible to enter a nonexistent sales agent’s name and phone number into the CUSTOMER file, but customers are not likely to be impressed if the insurance agency supplies the name and phone number of an agent who does not exist. Should the personnel manager allow a nonexistent agent to accrue bonuses"

class Question_10(Chapter_1):

    def __init__(self):
        super().__init__()
        self.numQ = 10
        self.question = "What happens when not all the required changes in the redundant data are made successfully?"
        self.solution = "Data Anomaly"
        self.description = "Any change in the any field value must be correctly made in many places to maintain data integrity. A data anomaly develops when not all of the required changes in the redundant data are made successfully.\nSome of the types are \"Update Anomalies\", \"Insertion Anomalies\" and \"Deletion Anomalies\""

# class Question_11(Chapter_1):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 11
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_12(Chapter_1):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 12
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_13(Chapter_1):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 13
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_14(Chapter_1):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 14
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_15(Chapter_1):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 15
#         self.question = ""
#         self.solution = ""
#         self.description = ""
