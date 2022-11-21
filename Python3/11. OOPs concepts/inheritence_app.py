# Heirarchical Inheritence

class Animal:
    def walk(self):
        print("Walking...")

class Dog(Animal): # class Child(Parent)
    pass           # pass is used, when we don't have anything to write in the class

class Cat(Animal):
    pass

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.walk()