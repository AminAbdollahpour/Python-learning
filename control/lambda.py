myfunction = lambda num: num * num
myfunction2 = lambda first, second: first + second

# print(myfunction(3))
# print(myfunction2(3, 4))
numbers = [1, 2, 3, 4, 5]
doubles = map(lambda num: num * 2, numbers)
print(list(doubles))
