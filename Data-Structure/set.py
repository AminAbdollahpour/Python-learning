numbers = {1, 2, 3, 4}
numbers_2 = {1, 'p', 3, 'a', 1, 5, 7}
# print(numbers_2)
# if list gets converted to a set its duplicates get removed just like set to list
numbers.add(5)  # if it's already in it nothing happens
numbers.remove(2)  # if it's not in it you get error
numbers.discard(2)  # same as remove but wont get error
numbers_copy = numbers.copy()
# numbers.clear()
set1 = {'ali', 'mansour', 'ghasem'}
set2 = {'davood', 'mansour', 'ghasem'}
print(set1 | set2)  # all in one
print(set1 & set2)  # in both
