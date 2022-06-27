from Template import Template
from random import shuffle
# when adding questions, update numQuestions and return_questions

# –––––––––––––––––––––––––Chapter 5–––––––––––––––––––––––––

class Chapter_5(Template):

    def __init__(self):
        super().__init__()
        self.chapter = 5
        self.chapter_name = "Advanced Join Modeling"
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

class Question_1(Chapter_5):

    def __init__(self):
        super().__init__()
        self.numQ = 1
        self.chapter = 5
        self.chapter_name = "Advanced Join Modeling"
        self.numQuestions = 10
        self.question = "Which model adds semantics to the ER model via entity supertypes, subtypes, and clusters?"
        self.solution = "EER"
        self.description = "The extended entity relationship (EER) model adds semantics to the ER model via entity supertypes, subtypes, and clusters. An entity supertype is a generic entity type that is related to one or more entity subtypes."

class Question_2(Chapter_5):

    def __init__(self):
        super().__init__()
        self.numQ = 2
        self.chapter = 5
        self.chapter_name = "Advanced Join Modeling"
        self.numQuestions = 10
        self.question = "What depicts the arrangement and relationships between entity supertypes and entity subtypes?"
        self.solution = "Specialization Hierarchy"
        self.description = "A specialization hierarchy depicts the arrangement and relationships between entity supertypes and entity subtypes. Inheritance means that an entity subtype inherits the attributes and relationships of the supertype. Subtypes can be disjoint or overlapping. A subtype discriminator is used to determine to which entity subtype the supertype occurrence is related. The subtypes can exhibit partial or total completeness. There are basically two approaches to developing a specialization hierarchy of entity supertypes and subtypes: specialization and generalization."

class Question_3(Chapter_5):

    def __init__(self):
        super().__init__()
        self.numQ = 3
        self.chapter = 5
        self.chapter_name = "Advanced Join Modeling"
        self.numQuestions = 10
        self.question = "What is a “virtual” entity type used to represent multiple entities and relationships in the ERD?"
        self.solution = "Entity Cluster"
        self.description = "An entity cluster is a “virtual” entity type used to represent multiple entities and relationships in the ERD. An entity cluster is formed by combining multiple interrelated entities and relationships into a single, abstract entity object."

class Question_4(Chapter_5):

    def __init__(self):
        super().__init__()
        self.numQ = 4
        self.chapter = 5
        self.chapter_name = "Advanced Join Modeling"
        self.numQuestions = 10
        self.question = "What are identifiers that exist in the real world?"
        self.solution = "Natural Keys"
        self.description = "Natural keys are identifiers that exist in the real world. Natural keys sometimes make good primary keys, but not always. Primary keys must have unique values, they should be non-intelligent, they must not change over time, and they are preferably numeric and composed of a single attribute."

class Question_5(Chapter_5):

    def __init__(self):
        super().__init__()
        self.numQ = 5
        self.chapter = 5
        self.chapter_name = "Advanced Join Modeling"
        self.numQuestions = 10
        self.question = "What is a candidate key that consists of two or more attributes that together uniquely identify an entity occurrence?"
        self.solution = "Composite Keys"
        self.description = "A composite key, in the context of relational databases, is a combination of two or more columns in a table that can be used to uniquely identify each row in the table. Uniqueness is only guaranteed when the columns are combined; when taken individually the columns do not guarantee uniqueness."

class Question_6(Chapter_5):

    def __init__(self):
        super().__init__()
        self.numQ = 6
        self.chapter = 5
        self.chapter_name = "Advanced Join Modeling"
        self.numQuestions = 10
        self.question = "What are useful when there is no natural key that makes a suitable primary key?"
        self.solution = "Surrogate Primary Keys"
        self.description = "Surrogate primary keys are useful when there is no natural key that makes a suitable primary key, when the primary key is a composite primary key with multiple data types, or when the primary key is too long to be usable."

class Question_7(Chapter_5):

    def __init__(self):
        super().__init__()
        self.numQ = 7
        self.chapter = 5
        self.chapter_name = "Advanced Join Modeling"
        self.numQuestions = 10
        self.question = "What refers to data whose values change over time and require that you keep a history of data changes?"
        self.solution = "Time-variant data"
        self.description = "Time-variant data refers to data whose values change over time and require that you keep a history of data changes. To maintain the history of time-variant data, you must create an entity that contains the new value, the date of change, and any other time-relevant data. This entity maintains a 1:M relationship with the entity for which the history is to be maintained."

class Question_8(Chapter_5):

    def __init__(self):
        super().__init__()
        self.numQ = 8
        self.chapter = 5
        self.chapter_name = "Advanced Join Modeling"
        self.numQuestions = 10
        self.question = "What occurs when you have one entity in two 1:M relationships to other entities, and there is an association among the other entities that is not expressed in the model?"
        self.solution = "Fan Trap"
        self.description = "A fan trap occurs when you have one entity in two 1:M relationships to other entities, and there is an association among the other entities that is not expressed in the model. Redundant relationships occur when there are multiple relationship paths between related entities. The main concern with redundant relationships is that they remain consistent across the model."

class Question_9(Chapter_5):

    def __init__(self):
        super().__init__()
        self.numQ = 9
        self.chapter = 5
        self.chapter_name = "Advanced Join Modeling"
        self.numQuestions = 10
        self.question = "What is an entity type that has got a relationship with one or more subtypes and it contains attributes that are common to its subtypes?"
        self.solution = "Supertype"
        self.description = "Supertype is an entity type that has got relationship (parent ot child relationship) with one or more subtypes and it contains attributes that are common to its subtypes."

class Question_10(Chapter_5):

    def __init__(self):
        super().__init__()
        self.numQ = 10
        self.chapter = 5
        self.chapter_name = "Advanced Join Modeling"
        self.numQuestions = 10
        self.question = "What are subgroups of the supertype entity and have unique attributes, but are different from each subgroup?"
        self.solution = "Subtypes"
        self.description = "Subtypes are subgroups of the supertype entity and have unique attributes, but are different from each subtype."

# class Question_11(Chapter_5):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 11
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_12(Chapter_5):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 12
#         self.question = ""
#         self.solution = ""
#         self.description = ""
#
# class Question_13(Chapter_5):
#
#     def __init__(self):
#         super().__init__()
#         self.numQ = 13
#         self.question = ""
#         self.solution = ""
#         self.description = ""
