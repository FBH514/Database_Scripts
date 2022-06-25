from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 16–––––––––––––––––––––––––
class Chapter_16(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 16
        self.chapter_name = "Database Administration and Security"
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

class Question_1(Chapter_16):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 16
        self.chapter_name = "Database Administration and Security"
        self.numQuestions = 7
        self.question = "What is a critical activity for any organization?"
        self.solution = "Data management"
        self.description = "Data management is a critical activity for any organization, so data must be treated as a corporate asset. The value of a data set is measured by the utility of the information derived from it. Good data management is likely to produce good information, which is the basis for better decision making."

class Question_2(Chapter_16):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 16
        self.chapter_name = "Database Administration and Security"
        self.numQuestions = 7
        self.question = "What is a comprehensive approach to ensure the accuracy, validity, and timeliness of data."
        self.solution = "Data quality"
        self.description = "Data quality is a comprehensive approach to ensure the accuracy, validity, and timeliness of data. Data quality focuses on correcting dirty data, preventing future inaccuracies in the data, and building user confidence in the data."

class Question_3(Chapter_16):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 16
        self.chapter_name = "Database Administration and Security"
        self.numQuestions = 7
        self.question = "Name the most commonly used tool for corporate data management"
        self.solution = "DBMS"
        self.description = "The DBMS is the most commonly used tool for corporate data management. The DBMS supports strategic, tactical, and operational decision making at all levels of the organization. The introduction of a DBMS into an organization is a delicate job; the impact of the DBMS on the organization’s managerial and cultural framework must be carefully examined."

class Question_4(Chapter_16):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 16
        self.chapter_name = "Database Administration and Security"
        self.numQuestions = 7
        self.question = "Who is responsible for managing the corporate database?"
        self.solution = "database administrator"
        self.description = " The database administrator (DBA) is responsible for managing the corporate data- base. The internal organization of database administration varies from company to company. Although no standard exists, it is common practice to divide DBA operations according to phases of the Database Life Cycle. Some companies have created a position with a broader mandate to manage computerized data and other data; this activity is handled by the data administrator (DA)."

class Question_5(Chapter_16):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.chapter = 16
        self.chapter_name = "Database Administration and Security"
        self.numQuestions = 7
        self.question = "What refers to activities and measures that ensure the confidentiality, integrity, and availability of an information system and its main asset, data?"
        self.solution = "Security"
        self.description = "Security refers to activities and measures that ensure the confidentiality, integrity, and availability of an information system and its main asset, data. A security policy is a collection of standards, policies, and practices that guarantee the security of a system and ensure auditing and compliance."

class Question_6(Chapter_16):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.chapter = 16
        self.chapter_name = "Database Administration and Security"
        self.numQuestions = 7
        self.question = "What is a weakness in a system component that could be exploited to allow unauthorized access or service disruption?"
        self.solution = "security vulnerability"
        self.description = "A security vulnerability is a weakness in a system component that could be exploited to allow unauthorized access or service disruption. A security threat is an imminent security violation caused by an unchecked vulnerability. Security vulnerabilities exist in all components of an information system: people, hardware, software, network, procedures, and data. Therefore, it is critical to have robust database security. Database security refers to DBMS features and related measures that comply with the organization’s security requirements."

class Question_7(Chapter_16):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.chapter = 16
        self.chapter_name = "Database Administration and Security"
        self.numQuestions = 7
        self.question = "What requires a detailed analysis of company goals, its situation, and its business needs?"
        self.solution = " strategic plan"
        self.description = "The development of a data administration strategy is closely related to the company’s mission and objectives. Therefore, the strategic plan requires a detailed analysis of company goals, its situation, and its business needs. To guide the development of this data administration plan, an integrating methodology is required. The most commonly used integrating methodology is known as information engineering (IE)."

# class Question_8(Chapter_16):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 8
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_9(Chapter_16):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 9
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_10(Chapter_16):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 10
#         self.question = ""
#         self.solution = ""
#         self.description = ""
