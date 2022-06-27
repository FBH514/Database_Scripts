from Template import Template
from random import shuffle


# –––––––––––––––––––––––––Chapter 14–––––––––––––––––––––––––

class Chapter_14(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 14
        self.chapter_name = "Big Data and NoSQL"
        self.numQuestions = 4

    @staticmethod
    def return_questions():
        q1 = Question_1()
        q2 = Question_2()
        q3 = Question_3()
        q4 = Question_4()

        question_list = [q1, q2, q3, q4]
        shuffle(question_list)
        return question_list

class Question_1(Chapter_14):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 14
        self.chapter_name = "Big Data and NoSQL"
        self.numQuestions = 4
        self.question = "What is characterized by data of such volume, velocity, and/or variety that the relational model struggles to adapt to it?"
        self.solution = "Big Data"
        self.description = "Big Data is characterized by data of such volume, velocity, and/or variety that the relational model struggles to adapt to it. Volume refers to the quantity of data that must be stored. Velocity refers to both the speed at which data is entering storage as well as the speed with which it must be processed. Variety refers to the lack of uniformity in the structure of the data being stored. As a result of Big Data, organizations are having to employ a variety of data storage solutions that include technologies in addition to relational databases, a situation referred to as polyglot persistence."

class Question_2(Chapter_14):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 14
        self.chapter_name = "Big Data and NoSQL"
        self.numQuestions = 4
        self.question = "What are based on graph theory and represent data through nodes, edges, and properties?"
        self.solution = "Graph Databases"
        self.description = "Graph databases are based on graph theory and represent data through nodes, edges, and properties. A node is similar to an instance of an entity in the relational model. Edges are the relationships between nodes. Both nodes and edges can have proper- ties, which are attributes that describe the corresponding node or edge. Graph data- bases excel at tracking data that is highly interrelated, such as social media data. Due to the many relationships among the nodes, it is difficult to distribute a graph data- base across a cluster in a highly distributed manner."

class Question_3(Chapter_14):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 14
        self.chapter_name = "Big Data and NoSQL"
        self.numQuestions = 4
        self.question = "Which type of databases also store data in key-value pairs, but the data in the value component is an encoded document?"
        self.solution = "Document Databases"
        self.description = "Document databases also store data in key-value pairs, but the data in the value component is an encoded document. The document must be encoded using tags, such as in XML or JSON. The DBMS is aware of the tags in the documents, which makes querying on tags possible. Document databases expect documents to be self- contained and relatively independent of each other."

class Question_4(Chapter_14):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 14
        self.chapter_name = "Big Data and NoSQL"
        self.numQuestions = 4
        self.question = "Name a document database that stores documents in JSON format."
        self.solution = "MongoDB"
        self.description = "MongoDB is a document database that stores documents in JSON format. The documents can be created, updated, deleted, and queried using a JavaScript-like language, named MongoDB Query Language. Data retrieval is done primarily through the find() method."

# class Question_5(Chapter_14):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 5
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_6(Chapter_14):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 6
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_7(Chapter_14):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 7
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_8(Chapter_14):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 8
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_9(Chapter_14):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 9
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_10(Chapter_14):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 10
#         self.question = ""
#         self.solution = ""
#         self.description = ""
