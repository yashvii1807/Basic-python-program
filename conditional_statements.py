#conditional statements

# if-elif-else(syntax)

# if(condition):
#     statement1
# elif(condition):
#     statement2
# else:
#     statementN      
  
# num = 5
# if(num > 2):
#     print("greater than 2")
# if(num >3):
#     print("greater than 3")    



# age = 19
# if(age >=18):
#    print("can vote") 
# else:
#     print("can't vote")

#note: Python uses indentation to define blocks of code. 
# and python in conditional statements use in first of all if condition is mandatory. 
# if or elif many times use this condition but else only one time use in conditional statements.


# marks = int(input("enter student marks :")) 

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks <80):
#     grade = "C"
# else:
#     grade = "D"
# print("grade of the studens ->", grade)   


#nested if else

# age = int(input("enter yor age :"))
# if (age >= 18):
#     if(age >= 80):
#         print("sorry you can't drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

#practice que

# 1 : write a program to check if a number entered by the user is odd or even

# num = int(input("enter a number : "))
# if (num % 2 == 0 ):
#     print("number is even")
# else:
#     print("number is odd")

# 2  :write a program to find the greatest of 3 numbers entered by the user

# num1 = int(input("enter first number :"))
# num2 = int(input("enter second number :"))
# num3 = int(input("enter third number :"))

# if(num1 >= num2)and(num1 >= num3):
#     print("first number is greatest :" , num1)
# elif(num2 >= num1)and (num2 >= num3):
#     print("second number is greatest :" , num2) 
# else:
#     print("third number is greatest :", num3)       

#write a program to check if a number is a multiple of 7 or not.

num = int(input("enter your number :"))
if(num % 7 == 0):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")    