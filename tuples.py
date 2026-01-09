#tuple in python
#A build in data type that us create immutable sequences of values

# tup = (2 , 1 , 3 , 1)
# print(type(tup))
# print(tup[3])

#tuple methods
# tup = (2 ,1 , 3, 2 , 2)
# print(tup.index(1))

# print(tup.count(2))


#practice que
# 1 write a program to ask the user to enter names of their 3 favorite movies & them in a list.

# movies =[]
# mov1 = input("enter 1st movie :")
# mov2 = input("enter 2nd movie :")
# mov3 = input("enter 3rd movie :")

# movies.append(mov1,)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# 2 write a program to check if a list contains a palideome of elemnts.(hint:use copy()method)

# list1 = [1, 2, 3]
# list2 = [1, 2, 3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("Palindrome")
# else:
#     print("Not palindrome")    

# 3 WAP to count the number of students with the "A" grade in the following tuple

# tuple = ["A", "B", "D", "C", "A", "A"]
# print(tuple.count("A"))

# 4 store the above values in a list & sort them from "A" to "D"
list = ["A", "B", "D", "C", "A", "A"]
list.sort()
list.sort(reverse =True)
print(list)

