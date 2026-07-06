#iterators: iterators are objects that allow you to traverse through a collection of elements, such as lists, tuples, or dictionaries. In Python, an iterator is an object that implements the iterator protocol, which consists of two methods: __iter__() and __next__().
#iterators are advanced python concepts that allow for efficient looping and memory management. Iterators provide a way to access elements of collection sequentially without exposing the underlying sturcture.

my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print(i)

type (my_list)  # Output: <class 'list'>
print(my_list)  # Output: [1, 2, 3, 4, 5]


##iterator 
iterator = iter(my_list)
print(type(iterator))  # Output: <class 'list_iterator'>
next(iterator)  # Output: 1
next(iterator)  # Output: 2