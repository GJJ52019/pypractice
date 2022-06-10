#classes and objects basics
#classes and object are used to represent real world things
#makes a new data type for the real world example

#classes are data types objects are memebers of the class

class Alien:
    #name is string, apendages int, diet will be a choice, is_a_threat is bool
    #use self.variable to assign the variables that are passed in
    def __init__(self, name, apendages, diet, is_a_threat): # defines self what attributes it should have
        self.name = name
        self.apendages = apendages
        self.diet = diet
        self.is_a_threat = is_a_threat

