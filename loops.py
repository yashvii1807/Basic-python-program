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
tup = (1,4,9,16,25,36,49,64,81,100,36)
 
x = 36
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("FOUND at idx" , i)
        break
    else:
        print("Finding....")    
    i += 1     
print("end of loop")    



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