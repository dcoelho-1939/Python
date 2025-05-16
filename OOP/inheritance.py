# Inheritance is the possibility of a class to inherit data from a 
# "mother" class.

# For example:
class Animal:
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def get_animaltype(self):
        return f"Type: {self.animal_type}"

class Horse(Animal):
    def __init__(self, name):
        animal_type = "Horse"
        self.name = name
        super().__init__(animal_type)
    
    def get_name(self):
        return f"Name: {self.name}"
    
class Dog(Animal):
    def __init__(self, name):
        animal_type = "Dog"
        self.name = name
        super().__init__(animal_type)

    def get_name(self):
        return f"Name: {self.name}"


animal1 = Horse("Bojack")
print(animal1.get_animaltype())
print(animal1.get_name())

print()

animal2 = Dog("Whatever")
print(animal2.get_animaltype())
print(animal2.get_name())
