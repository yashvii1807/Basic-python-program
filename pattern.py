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


n = 4
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() 