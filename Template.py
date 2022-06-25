import random


# –––––––––––––––––––––––––Template–––––––––––––––––––––––––

class Template:

    def __init__(self):
        self.count = None
        self.char = None
        self.chapter = None
        self.numQuestions = None
        self.numQ = None
        self.question = None
        self.answer = None
        self.solution = None
        self.description = None
        self.valid = None

    def beautify(self, char):
        self.char = char
        print((char*"–")*2)
        print()

    def compliments(self):
        nice_list = ['Great Job!', 'Well Done', 'Keep up the hard work!', 'Sweeeeet']
        emoji_list = ['🙏', '👀', '🔥', '💪', '🎉', '🌊', '✨', '🤗', '😎', '☀️']
        return f"{random.choice(emoji_list)} {random.choice(nice_list)}"

    def invalid_answer(self):
        return "Invalid Answer!"

    def grade(self, count):
        self.count = count
        grading = (count*100)/self.numQuestions
        # res = "{:.2f}".format(fnum)
        return f'''{"{:.2f}".format(grading)}%!'''

    def user_input(self):
        user_input = input("Type \"Yes\" to Continue ––> ")
        return user_input

    def main(self):
        self.beautify(25)
        print(f"Welcome to chapter {self.chapter}\nChapter {self.chapter} has {self.numQuestions} Questions")

        while True:
            if self.user_input() == "yes".casefold():
                print("\n–––Shuffling Questions–––")
                self.beautify(15)
                break
            else:
                continue
