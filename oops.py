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

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_number = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount, "was debited from your account.")  
        print("Your current balance is: Rs.", self.get_balance())  

    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount, "was credited to your account.")  
        print("Your current balance is: Rs.", self.get_balance())  

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, "123456789")
print(acc1.balance) # Output: 10000
print(acc1.account_number) # Output: 123456789
acc1.debit(200) # Output: Rs. 200 was debited from your
acc1.credit(500) # Output: Rs. 500 was credited to your account.