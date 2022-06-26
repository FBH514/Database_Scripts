from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 13–––––––––––––––––––––––––

class Chapter_13(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 13
        self.chapter_name = "Business Intelligence and Data Warehouses"
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

class Question_1(Chapter_13):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 13
        self.chapter_name = "Business Intelligence and Data Warehouses"
        self.numQuestions = 8
        self.question = "What describes a comprehensive, cohesive, and integrated set of tools and processes used to capture, collect, integrate, store, and analyze data with the purpose of generating and presenting information to support business decision making?"
        self.solution = "Business Intelligence"
        self.description = "Business intelligence (BI) is a term for a comprehensive, cohesive, and integrated set of applications used to capture, collect, integrate, store, and analyze data with the purpose of generating and presenting information to support business decision making."

class Question_2(Chapter_13):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 13
        self.chapter_name = "Business Intelligence and Data Warehouses"
        self.numQuestions = 8
        self.question = "What refers to an arrangement of computerized tools used to assist managerial decision making within a business?"
        self.solution = "Decision support systems (DSSs)"
        self.description = "Decision support systems (DSSs) refer to an arrangement of computerized tools used to assist managerial decision making within a business. DSSs were the original precursor of current-generation BI systems."

class Question_3(Chapter_13):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 13
        self.chapter_name = "Business Intelligence and Data Warehouses"
        self.numQuestions = 8
        self.question = "What is a data-modeling technique used to map multidimensional decision support data into a relational database for advanced data analysis?"
        self.solution = "Star Schema"
        self.description = "The star schema is a data-modeling technique used to map multidimensional decision support data into a relational database for advanced data analysis. The basic star schema has four components: facts, dimensions, attributes, and attribute hierarchies. Facts are numeric measurements or values that represent a specific business aspect or activity. Dimensions are general qualifying categories that provide additional perspectives to facts. Conceptually, the multidimensional data model is best represented by a three-dimensional cube. Attributes can be ordered in well-defined hierarchies, which provide a top-down organization that is used for two main purposes: to permit aggregation and provide drill-down and roll-up data analysis."

class Question_4(Chapter_13):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 13
        self.chapter_name = "Business Intelligence and Data Warehouses"
        self.numQuestions = 8
        self.question = "What refers to an advanced data analysis environment that supports decision making, business modeling, and operations research?"
        self.solution = "Online analytical processing (OLAP)"
        self.description = "Online analytical processing (OLAP) refers to an advanced data analysis environment that supports decision making, business modeling, and operations research."

class Question_5(Chapter_13):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.chapter = 13
        self.chapter_name = "Business Intelligence and Data Warehouses"
        self.numQuestions = 8
        self.question = "What is a subset of BI functionality that provides advanced data analysis tools to extract knowledge from business data?"
        self.solution = "Data analytics"
        self.description = "Data analytics is a subset of BI functionality that provides advanced data analysis tools to extract knowledge from business data. Data analytics can be divided into explanatory and predictive analytics."

class Question_6(Chapter_13):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.chapter = 13
        self.chapter_name = "Business Intelligence and Data Warehouses"
        self.numQuestions = 8
        self.question = "What focuses on discovering and explaining data characteristics and relationships?"
        self.solution = "Explanatory analytics"
        self.description = "Explanatory analytics focuses on discovering and explaining data characteristics and relationships."

class Question_7(Chapter_13):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.chapter = 13
        self.chapter_name = "Business Intelligence and Data Warehouses"
        self.numQuestions = 8
        self.question = "What focuses on creating models to predict future outcomes or events based on the existing data?"
        self.solution = "Predictive analytics"
        self.description = "Predictive analytics focuses on creating models to predict future outcomes or events based on the existing data."

class Question_8(Chapter_13):

    def __init__(self):
        super().__init__()
        self.numQ = 8
        self.chapter = 13
        self.chapter_name = "Business Intelligence and Data Warehouses"
        self.numQuestions = 8
        self.question = "What automates the analysis of operational data to find previously unknown data characteristics, relationships, dependencies, and trends?"
        self.solution = "Data mining"
        self.description = "Data mining automates the analysis of operational data to find previously unknown data characteristics, relationships, dependencies, and trends. The data-mining process has four phases: data preparation, data analysis and classification, knowledge acquisition, and prognosis."

# class Question_9(Chapter_13):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 9
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_10(Chapter_13):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 10
#         self.question = ""
#         self.solution = ""
#         self.description = ""
