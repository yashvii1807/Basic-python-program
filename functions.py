#functions
#Block of statements that perform a specific task.
#def function_name(parameters):

# def func_name(parameters1, parameters2):
#function body
    
# a = 5
# b = 10

# sum = a + b
# print("Sum =", sum)

# def calculate_sum(a,b):
#     sum = a + b
#     print(sum)
#     return(sum)

# calculate_sum(12,24)
# calculate_sum(45,64)
# calculate_sum(76,23)


#function defination
# def calculate_sum(a , b): #parameters
#     return a + b
# sum = calculate_sum(3432,435)#function call with arguments
# print(sum)

# def print_hello():
#     print("hello")

# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()

# def print_hello():
#     print("hello")

# output = print_hello()
# print(output)   #prints None because the function does not return any value
 
#avg of 3 number

# def calc_sum(a,b,c):
#     sum = a + b + c
#     average = sum / 3
#     print(average)
#     return average

# calc_sum(12,45,78)

#there are 2 types of functions :
# 1. built-in function
# 2. user-defined function

#built-in function
# print() , len() , type() , range()  

#example
# print("yashvi")#sepace: #this is a built-in function that prints the output to the console.
# print("sidapara")#end:

# print("yashvi",end=" ")
# print("sidapara")

#default parameters
#Assiging default values to parameters , which is used when no argument is passed.

# def cal_prod(a=3,b=3):#parameters with default values
#     print(a * b )
#     return a * b

# cal_prod()#passing arguments

#practice que
#write a function to print the length of a list. (list is the parameter)

# ex1
# def print_length(lst):
#     print(len(lst))
#     return len(lst)

# print_length([1 ,2 , 3, 4 ,5 , 5])

#ex2
# cities = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"]
# heroes = ["Ironman", "Spiderman", "Hulk", "Thor", "Captain America"]

# def print_list(lst):
#     print(len(lst))

# print_list(cities)
# print_list(heroes)

#write a function to print the elements of a list in  single line(line is the parameter)
# cities = ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"]
# heroes = ["Ironman", "Spiderman", "Hulk", "Thor", "Captain America"]

# def print_list(lst):
#     for item in lst:
#         print(item , end=" ")

# print_list(heroes)
# print()

#write a function to find the factorial of n.(n is the parameter)
# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
#     print(fact)

# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)
        
# fact(5)
# fact(0)
# fact(10)    

#write a function to convert USD to INR(usd_value is the parameter)

# def converter(usd_value):
#     inr_value = usd_value * 90.44
#     print(usd_value, "USD =" , inr_value, "INR")

# converter(100)
# converter(45)    


#write a function to user input check number is even or odd . (n is the parameter)

# def check_even_odd(i):
#     if n % 2 == 0:
#         print(n, "is EVEN")
#     else:
#         print(n, "is ODD")
#     return
# n = int(input("enter a number: "))
# check_even_odd(n)        
    



#Recursion
#when a function calls itslf repeatedly.

# def show(n):
#     if(n == 0): #base case
#         return
#     print(n)
#     show(n-1)
#     print("END")
# show(5)


# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n

# print(fact(6))
    

#practice que
#write a recursive function to calculate the sum of frist n natural numbers.

# def sum(n):
#     if n == 0:
#         return 0
#     return sum(n-1) + n 

# result = sum(10)
# print("sum of first n natural number =" , result)



#write a recursive function to print all elements in all list
#hint : use list & index as parameters.

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "apple" , "banana", "guava", "litchi"] 

print_list(fruits)
