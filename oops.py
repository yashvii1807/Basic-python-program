#oops
# to map with  real world scenarios we use oops in code
#this is called object oriented programming

#class  &  objects
# class is a blueprint of an object

# class student:
#     name = "Rohit"
# s1 = student() #object creation
# print(s1.name) #accessing the property of class using object    

# class car:
#     color = "red"
#     brand = "BMW"
# c1 = car() #object creation
# print(c1.color) #accessing the property of class using object    
# print(c1.brand)


#constructor
#all classes have a function called_init_() which is always executed when the class is being initiated. 

#the self parameter is a reference to the current instance of the class and is used to access variables that belong to the class.


# class students:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s1 = students("Rohit", 20)
# print(s1.name,s1.age)

# s2 = students("Rahul", 22)
# print(s2.name,s2.age)


#attributes----> data;variables

#class & instance attributes
#class attributes are shared by all instances of the class, while instance attributes are unique to each

# 1 = class.attr
# 2 = instance.attr

# class students:
#    college_name = "rk university" #class attribute
#    def __init__(self, name, marks):
#        self.name = name #instance attribute
#        self.marks = marks #instance attribute
# s1 = students("Rohit", 90)
# s2 = students("Rahul", 95)
# print(s1.name, s1.marks)
# print(s2.name, s2.marks)

# print(students.college_name) #accessing class attribute




#methods : methods are functions that belong to objects.

# def welcome(self):
#     print("welcome to students")



# create student class that takes name &  makrs of 3 students as arguments in constructor. then create a method to print the average.
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_average(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your average marks is:", sum/3)
# s1 = Student("Rohit", [90, 80, 70])
# s1.get_average()

 

#static methods: 
#methods that dont use the self parameter( work at class level )

# class Student:
#     @staticmethod       #decorator
#     def welcome():
#         print("welcome to students")

#decorators are allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.        


#Abstraction
#hiding the implementation details of class and only showing the essential features of the class to the user is called abstraction.


#Ex:
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brake = False
#         self.clutch = False
#     def start(self):
#         self.acc = True
#         self.clutch = True
#         print("car started...")
# car1 = Car()
# car1.start()        


#Encapsulation
#wrapping up of data and methods into a single unit is called encapsulation. (object-oriented programming)

#Que:
#1 create Account class with 2 attributes - balance & account number.create methods for debit , credit & print the balance.

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_number = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.",amount, "was debited from your account.")  
#         print("Your current balance is: Rs.", self.get_balance())  

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.",amount, "was credited to your account.")  
#         print("Your current balance is: Rs.", self.get_balance())  

#     def get_balance(self):
#         return self.balance
    
# acc1 = Account(10000, "123456789")
# print(acc1.balance) # Output: 10000
# print(acc1.account_number) # Output: 123456789
# acc1.debit(200) # Output: Rs. 200 was debited from your
# acc1.credit(500) # Output: Rs. 500 was credited to your account.


# del keyword : used to delete object properties or objects itself.

# del s1.name #deleting the name property of s1 object
# del s1 #deleting the s1 object itself


#example:
# class Student:
#     def __init__(self, name):
#         self.name = name
# s1 = Student("Rohit")
# print(s1.name) # Output: Rohit    
# del s1.name
# print(s1.name)



# private (like) attrubutes & methods

# conceptual implementation in python:
# private attributes & method are meant to be used only within the class and not accessible from outside the class. 

#ex:
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("12345", "abcde")          
# print(acc1.acc_no) # Output: 12345
# #print(acc1.__acc_pass) # Output: AttributeError: 'Account' object has no attribute '__acc_pass'
# print(acc1.reset_pass()) # Output: abcde


#inheritance
#when one class (child/derived)derives the properites & method of another class(parent/base)
# 1. single inheritance: when a child class inherits from a single parent class.
# 2. multiple inheritance: when a child class inherits from multiple parent classes.
# 3. multilevel inheritance: when a child class inherits from a parent class, which in turn inherits from another parent class.


# class car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(car):
#     def __init__(self, name):        
#         self.name = name

# car1 = ToyotaCar("Camry")
# car2=  ToyotaCar("Corolla")

# print(car1.start())

# # 2. multiple inheritance
# class A:
#     varA = "I am from class A"

# class B:
#     varB = "I am from class B"

# class C(A, B):
#     varC = "I am from class C" 
# c1 = C()
# print(c1.varA) # Output: I am from class A
# print(c1.varB) # Output: I am from class B
# print(c1.varC) # Output: I am from class C


#Super() method: used to call the parent class constructor from the child class constructor.



# class car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class ToyotaCar(car):
#     def __init__(self, name, type):   
#         super().__init__(type)     
#         self.name = name
#         super().start() 
       

# car1 = ToyotaCar("Camry", "Sedan")
# print(car1.type)        



#Class method
#A class method  is bound to the class & receives the class as an implicit first argument. It can be called on the class itself or on an instance of the class.

#note: static method cant access or modify class state & generally for utility.

# class Student:
#     @classmethod
#     def college(cls):
#         pass


   #method-1 
# class person:
#     name = "anonymous"

#     #def changeName(self,name):
#         #person.name = name #this is class attribute so we can access it using class name
#         #self.name = name #this is instance attribute so we can access it using self
#         #self.__class__.name = "yashvi" #this is also class attribute so we can access it using self.__class__.name

#     @classmethod
#     def changeName(cls,name):
#         cls.name = name #this is class attribute so we can access it using cls

# p1 = person()
# p1.changeName("yashvi")
# print(p1.name)
# print(person.name)


# 1. static method: this method is don't have access to class or instance attributes. it is used for utility purpose.
# 2. class method: this method is bound to the class & receives the class as an implicit first argument.
# 3. instance method: this method is bound to the instance of the class & receives the instance as an implicit first argument.


#property decorator: we use @property decorator on any method in the class to use the method as a property.
# class Student:
#     def __init__(self, phy , chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#     #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

#     # def calcupercentage(self):
#     #     self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"


#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"


# stu1 = Student(90, 97, 99)
# print(stu1.percentage)        

# # stu1.phy = 54
# # print(stu1.phy)
# # stu1.calcupercentage()
# print(stu1.percentage)



