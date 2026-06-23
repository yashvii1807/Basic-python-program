# Reverse string in Python

text = input("Enter string: ")

reverse_text = text[::-1]

print("Reversed string is:", reverse_text)


# Prime or Not Prime in Python

num = int(input("Enter number: "))

if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# Fibonacci Series in Python

n = int(input("Enter how many terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


# Factorial of a Number in Python

num = int(input("Enter number: "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial is:", fact)


# Palindrome String in Python

text = input("Enter string: ")

rev = text[::-1]

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# Sum of Array Elements in Python

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

total = sum(arr)

print("Sum of array elements is:", total)


# Largest Element in Array in Python

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = max(arr)

print("Largest element is:", largest)


# Linear Search in Python

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter number to search: "))

for i in range(n):
    if arr[i] == search:
        print("Element found at position:", i + 1)
        break
else:
    print("Element not found")


# Bubble Sort in Python

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted array is:", arr)



# Count Even and Odd Numbers in Python

num = int(input("enter a number : "))
if (num % 2 == 0 ):
    print("number is even")
else:
    print("number is odd")





# Pattern Programs in Python

n = int(input("Enter number of rows: "))

# 1. Star Square
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print()

# 2. Left Triangle
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# 3. Inverted Triangle
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# 4. Right Triangle
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

print()

# 5. Pyramid
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

print()

# 6. Reverse Pyramid
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

print()

# 7. Diamond
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

