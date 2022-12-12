from functools import reduce

## *args and *kwargs

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
print('-- Finished keyword args')

## Processing a dictionary
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)
print('-- Finished processing dictionary')


#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla', 'maya']

def caps(item):
    return item.capitalize()

print(list(map(caps,my_pets)))



#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def filterScores(item):
    return item > 50

print(list(filter(filterScores, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def totals(acc, item):
    return acc + item

print(reduce(totals, my_numbers + scores))

print(scores + my_numbers)