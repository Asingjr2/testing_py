"""Python class creation for generic testing."""


class Human(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @property
    def bio(self):
        return "My name is {} and I am {}.".format(self.name, self.age)



