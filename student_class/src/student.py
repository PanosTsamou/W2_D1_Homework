
class Student():

    #it initialises the class properties
    def __init__(self, input_studen_name, input_conhort):
        self.name = input_studen_name
        self.cohort = input_conhort

    #it returns the string "I can talk!"
    def talk(self):
        return "I can talk!"

    #it takes the student's fav language  and puts in a string
    def say_favourite_language(self, coding_language):
        result = f'I love {coding_language}'
        return result
        

