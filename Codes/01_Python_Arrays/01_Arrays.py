
''' Note: Python does not have built-in support for Arrays, but Python Lists can be used instead. '''



# >>>>> ARRAYS EX.<<<<< # :
''' Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python 
you will have to import a library, like the NumPy library. '''

cars = ["Ford", "Volvo", "BMW"] # Array



# >>>>> WHAT IS ARRAY? <<<<< # :

''' An array can hold many values under a single name, and you can access the values by referring 
to an index number. '''



# >>>>> ACCESS THE ELEMENTS OF AN ARRAY <<<<< # :
''' Get the value of the first array item: '''

cars = ["Ford", "Volvo", "BMW"]

x = cars[0]
print(x) # Output: Ford



# >>>>> CHANAGING THE ARRAY ELEMENT <<<<< # :
''' Modify the value of the first array item: '''

cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota"
print(cars) # Output: ["Toyota", "Volvo", "BMW"]



# >>>>> LENGTH OF AN ARRAY <<<<< # :
cars = ["Ford", "Volvo", "BMW"]

print(len(cars)) # Output: 3



# >>>>> LOOPING THROUGH ARRAY ELEMENTS <<<<< # :
cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)
# Output: Ford
#         Volvo 
#         BMW



# >>>>> ADDING ARRAY ELEMENTS <<<<< # :
cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")
print(cars) # Output: ['Ford', 'Volvo', 'BMWk', 'Honda']



# >>>>> REMOVING ARRAY ELEMENTS <<<<< # :

#1: pop() method
cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)
print(cars) 

#2: remove() method
cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")
print(cars)



# >>>>> ARRAY METHODS <<<<< # :

'''
[METHODS]                        [DESCRIPTION] 

append()	   ::       Adds an element at the end of the list
clear()	     ::       Removes all the elements from the list
copy()	     ::       Returns a copy of the list
count()	     ::       Returns the number of elements with the specified value
extend()	   ::       Add the elements of a list (or any iterable), to the end of the current list
index()	     ::       Returns the index of the first element with the specified value
insert()	   ::       Adds an element at the specified position
pop()	       ::       Removes the element at the specified position
remove()	   ::       Removes the first item with the specified value
reverse()	   ::       Reverses the order of the list
sort()	     ::       Sorts the list

'''
