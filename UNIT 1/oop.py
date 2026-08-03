# 1
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
     
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

s1= student("John", 25)
s2 = student("Harsh", 20)

s1.display()
print()
s2.display()
print()

# 2
class collage:

    collage = "MIT ADT"
    def __init__(self,name):
        self.name = name

    def display(self):
        print("collage name:",self.collage)
        print("Name:",self.name)

s1 = collage("Sudhir")
s2 = collage("Harsh")

s1.display()
print()
s2.display()

#3
# instance method 

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

s1 = student("Rahul", 21)
s1.display()

# 4
# static method

class calculator:
    @staticmethod
    def add(x,y):
        return x+y

# class name
a = calculator.add(5,6)
print("Addition:",a)

# object
obj = calculator()
print("Addition:",obj.add(9,6))


# 5
# classes and objects

class car:
    def start(self):
        print("Car started")

car1 = car()
car1.start()
