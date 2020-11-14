class Animal:
    def __init__(self, age: int, gender: str):
        self.age = age
        self.gender = gender

    def is_mammal(self):
        pass


class Dog(Animal):

    def __init__(self, age: int, gender: str, color: str):
        super().__init__(age, gender)
        self.color = color

    def bark(self):
        pass

    def fetch(self):
        pass


class Zebra(Animal):

    def __init__(self, age: int, gender: str, is_wild: bool):
        super().__init__(age, gender)
        self.is_wild = is_wild

    def run(self):
        pass


class Duck(Animal):

    def __init__(self, age: int, gender: str, beak_color: str = "yellow"):
        super().__init__(age, gender)
        self.__beak_color = beak_color
        
    def swim(self):
        pass

    def fly(self):
        pass

    def quack(self):
        pass
