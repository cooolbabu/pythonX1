from functools import reduce

## map, filter, reduce
#1 MAP function
my_pets = ['sisi', 'bibi', 'titi', 'carla', 'maya']

def caps(item):
    return item.capitalize()

print(list(map(caps,my_pets))) ## Map takes a function and iterable as parameters

#3 Filter
scores = [73, 20, 65, 19, 76, 100, 88]

def filterScores(item):
    return item > 50

print(list(filter(filterScores, scores)))

#4 Zip function- if there is an extra .. it's omitted
player =["John", "Sam", "Jack", "Tom", "Mary", "Art", "Nick", "JoAnn"]
print(list(zip(player,scores)))

#Lambda programming
print(list(map(lambda pet: pet.capitalize(), my_pets)))
print((lambda pet: pet.capitalize(), my_pets))

## *args and *kwargs

def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
print('-- Finished keyword args')

## Processing a dictionary
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)
my_list4 = [num**2 for num in range(0,100) if num%2 ==0]
print(my_list4)
print('-- Finished processing dictionary')

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, my_numbers)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def totals(acc, item):
    return acc + item

print(reduce(totals, my_numbers + scores))

print(scores + my_numbers)

## Comprehension
simple_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}

my_dict = {k:v**2 for k,v in simple_dict.items() if v % 2 == 0}
print(my_dict)