
class Student():

    def __init__(self, input_studen_name, input_conhort):
        self.name = input_studen_name
        self.cohort = input_conhort

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, coding_language):
        result = f'I love {coding_language}'
        return result
        

