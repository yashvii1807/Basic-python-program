#Loops in Python

#loops are used to repeat instructions until a certain condition is met

#there are two main types of loops in python    

# 1. for loop   
# 2. while loop

# while loop
# syntax

# count = 1
# while count <= 5:
#     print("hello world")
#     count = count + 1
# print(count)

# note : make sure to update the condition variable inside the loop to avoid infinite loop

# i = 1

# while i <= 100000:
#     print("hello yashu",i)
#     i = i + 1
# print(i)

#print numbers from 1 to 10 using while loop
# i = 10
# while i >=1:
#     print(i)
#     i = i - 1   
# print("done")    


# print multiplication table of 13 using while loop
# i = 1
# while i <=10:
#     print(13, "x", i, "=", 13*i)
#     i += 1


#practice questions
#1 print numbers 1 to 100 
# i = 1
# while i<= 100:
#     print(i)
#     i += 1

#2 print numbers from 100 to 1
# i = 100
# while i>= 1:
#     print (i)
#     i-= 1

# 3 print the multiplication table of a number n
# i = 1
# n = int(input("Enter a number:"))
# while i <= 10:
#     print(n , "x", i , "=", n*i)
#     i+=1

# 4 print the elements of the following list using loop

# [1,4,9,16,25,36,49,64,81,100]
# i = 0
# num = [1,4,9,16,25,36,49,64,81,100]
# while i < len(num) :
#     print(num[i])
#     i+=1

# heros = ["ironman", "thor", "hulk", "captain america", "black widow"]
# i = 0
# while i < len(heros):
#     print(heros[i])
#     i += 1


    
# 5 search for a number x in this tuple using loop
# tup = (1,4,9,16,25,36,49,64,81,100,36)
 
# x = 36
# i = 0
# while i < len(tup):
#     if(tup[i] == x):
#         print("FOUND at idx" , i)
#         break
#     else:
#         print("Finding....")    
#     i += 1     
# print("end of loop")    



# break and continue

# break : used to terminate the loop when enumerated.

# continue : terminate execution in the current iteration & continues execution of the loop with the next iteration.

# i = 1
# while i<=5:
#     print(i)
#     if(i == 3):
#         break
#     i += 1
# print("end of loop")    



# i = 0
# while i<= 15:
#     if(i%2 !=0):
#     # if(i %2 == 0):   
#         i += 1
#         continue
#     print(i)
#     i += 1






# For loop

#loops are  used for sequntial traversal. for traversing list, string , tuples etc...

# names = ["y", "v", "s", "r"] 
# for val in names:
#     print(val)

# num = [1,2,3,4,5,6,7,8,9]
# for val in num:
#     print(val)

#iteratter upr kam krvu hoy to  while loop use thay
#and datatypes on traves to for loop use thay

# str = "yashuuu"
# for char in str:
#     print(char)
# else:
#     print("END")    



#practice que
#using for
#1     print the element of the following list using a loop:

# nums = [1,4,9,16,25,36,49,64,81,100]
# for val in nums:
#     print(val)


#2   search for a numer x in this tuple using loop:
nums = [1,4,9,16,25,36,49,64,81,100,49]

# user = int(input("enter the number : "))
# for i in nums:
#     if(i == user):
#         print("number found")

#         break
#     else:
#         print("searching..")

# x = 49
# i = 0
# for el in nums:
#     if (el == x):
#         print("number found at i", i)
#     i += 1



#RANGE() FUNCTION 
#range function returns a sequence of numbers , starting from 0 by default , and incremnet by 1(by default), and stop before a specified number
seq = range(10)
for i in seq:
    print(i)



