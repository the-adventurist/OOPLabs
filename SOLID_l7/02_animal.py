from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @abstractmethod
    def animal_sound(self):
        return ""


class Dog(Animal):
    def animal_sound(self):
        return "woof-woof"


class Cat(Animal):
    def animal_sound(self):
        return "meow"


class Chicken(Animal):
    def animal_sound(self):
        return "Cluck"



animals = [Cat('cat'), Dog('dog')]
for animal in animals:
    print(animal.animal_sound())

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]
for animal in animals:
    print(animal.animal_sound())