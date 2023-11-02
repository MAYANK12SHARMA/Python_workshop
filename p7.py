'''
Objects:

# ?Object in Python represent real-world entities. They are instance of classes. In the "Objects" example, We creat a DOGS Documnet class to represent dogs. The init method is a special method used to initialise the object when it's created . iN this case sets the name attribute of the object.

# !self is a reference to the current instance of a class. It sis used to interact with instance-specific  attribute and method making it a fundamental part of object-oriented programming in Pyhton.

# ? In the "Objeccts" and "Classes" examples, self is used within init method refer to the instance being created. It is convention  to name this parameter self, but you can technical name it something else if you prefer. The self parrameter is automatically passed to instamce method when they are called it allow you to set snd access the attributes of the objects.

'''



# # ? Creating an object 
# class Dog:
#     def __init__(self,name):
#         self.name = name 

# dog1 = Dog("Buddy")
# print(dog1.name)      #output :-  Buddy 



# classes

# ? classes in python are like blueprint for creating object.

# class car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model 
#         self.year = year 
        
# # creating the class 
# car1 = car("rolls roys","Phantom", "2023")
# car2 = car("Rolls roys", "Ghost", "2024")

# print(car1.make, car1.model, car1.year)
# print(car2.make, car2.model, car2.year)



# Encapuslation 

# IT is a concept that restrict the access to certain part of an object.

# class BankAccount:
#     def __init__(self, AC, balance):
#         self._AC = AC  # protected attribute
#         self.__balance = balance  # private attribute

#     def get_balance(self):
#         return self.__balance  # getter method to access private attribute

# account1 = BankAccount("12345", 10000)
# print(account1._AC)  # Output: 12345
# print(account1.get_balance())  # Output: 10000


# inheritance 

#  inheritacne allows you to create new classes that inherit properties  

# Base class (parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass  # Placeholder for the sound method


# Derived class (child class) inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Creating objects of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the make_sound method of derived classes
print(dog.name + ": " + dog.make_sound())  # Output: Buddy: Woof!
print(cat.name + ": " + cat.make_sound())  # Output: Whiskers: Meow!





