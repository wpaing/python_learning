class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def into(self):
        print(f"{self.name} is {self.age} years old")
person1=Person("Aung Aung",30)
person2=Person("Maung Maung",40)
person1.into()
person2.into()