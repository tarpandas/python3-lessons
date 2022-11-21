class Person:
    def __init__(self, name):
        self.name = name
    def talking(self):
        print(f"{self.name} is talking.")

person1 = Person("Amit")
person1.talking()

person2 = Person("Suresh")
person2.talking()