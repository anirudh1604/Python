'''An iterable is an object capable of returning its members one by one. SImply, it is anything that you can loop
over using a for loop .'''

'''An iterator is an object represnting stream of data. We can implement this using iter(). An iterator can be used
manually loop over the items in the iterable.'''


'''The repeated passing of the iterator to the built-in next function returns successive items in the stream. 
When the item is consumed from the iterator, it is gone, and eventually,
when no more data is available to retrieve, a StopIteration exception is raised.'''

my_list = [1, 2, 3]

my_iter_list = iter(my_list)

print(type(my_iter_list))

print(next(my_iter_list))
print(next(my_iter_list))
print(next(my_iter_list))
print(next(my_iter_list))

''' iterator is a more general concept: 
any object whose class has a next method (__next__ in Python 3) and an __iter__ method that does return self'''


