# n = 4
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()        

#ans
# * * * * 
# * * * * 
# * * * * 
# * * * *

# n = 6
# for i in range(n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()    

#ans
# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *



# n = 5
# for i in range(n, 0 , -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()   

#ans
# * * * * * 
# * * * * 
# * * *
# * *
# *    


# n = 4
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print() 




#heart pattern

for i in range(6):
    for j in range (7):
        if (i == 0 and j % 3 != 0) or \
        (i == 1 and j % 3 == 0) or \
        (i - j == 2) or \
        (i + j == 8):
          print("*", end="")
        else:
            print(" ", end="")
    print()              