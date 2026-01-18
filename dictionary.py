#dictionary are used to store data values in key:value pairs they are unordered , mutable (changeble) & dont allow  dublicate keys

# info = {
#     "key" : "value",
#     "name" : "yashvi",
#     "learning" : "python",
#     "age" : 20,
#     "is_adult" : True,
#     "marks" : 47.54,
#     "subjects" : ["python","C","java"],
#     "topics" : ("dict","set")
# }

# print(type(info))

# info["name"] = "vaibhavvv"
# info["surname"] = "chauhan"
# print(info)   

#nested directory
# students = {
#     "name" : "yashuu",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 98,
#         "math" : 95 
#     }
# }

# print((students["subjects"]))
# students.update({"age" : 20})
# print(students)
# new_dict = {"city" : "rajkot"}
# students.update(new_dict)
# print(students)



# #dictionary methods
# print(len(list(students.keys())))
# print(list(students.values()))

# pairs = list(students.items())
# print(pairs[0])

# print(students["name"]) # 
# print(students.get("name"))

# myDict.keys()  # returns all keys
# myDict.values() #return all values
# myDict.items() # return all (key , val) pair as tuples
# myDict.get("key") #return the key according to value
# myDict.update(newDict) #insert the specification to the dictionary




#practice que
#1 : store following word meaning in python dictionary
#table : "a pice of furnitre", "list of facts & figures"
#cat : "a small animal"

# yashvi = {
#     "table" :
#     ["a piece of furmiture , list of facts & figures"],
#     "cat" : { 
#         "cat": "a samll animal"
#     }
# }
# print(yashvi["table"])

# print(yashvi["cat"]["cat"])


#2 : wAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionry
#& add one by one . use subject name as key & marks as value

# marks = {}

# x = int(input("enter phy : "))
# marks.update({"phy": x})

# x = int(input("enter math : "))
# marks.update({"math": x})

# x = int(input("enter chem : "))
# marks.update({"chem": x})

# print(marks)


# 3 figure out a way to store 9 & 9.0 as seperate values in the set.
values = {
    ("float",9.0),
    ("int",9)
}
print(values)


