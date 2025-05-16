# With classes we can define a blueprint for how an object will work.
# In other words, we define the data an object contains, so that it is 
# able to interact with the program properly. An object can only exist
# through a class.

# Example:
class Person:
    """ This class defines a model for a person """

    def __init__(self, first_name, last_name, age, nationality):
        """ This is the constructor of the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
        self.nationality = nationality

    def get_alldata(self):
        print(f"""Full name: {self.get_fullname()} | Age: {self.get_age()} | Nationality: {self.get_nationality()}""")

    def get_fullname(self):
        """ This method gets the person's full name """ 
        return self.first_name + " " + self.last_name

    def get_age(self):
        return self.age 

    def get_nationality(self):
        return self.nationality

# Once you have the class, you can create objects from that class, that 
# will carry all the data you just defined and created.

person1 = Person("Davi", "Coelho", 24, "Brazilian")
print(person1.get_alldata())

# For every object created, every data will have different values:
person2 = Person("Nayara", "Louback", 23, "Brazilian")
print(person2.get_alldata())
