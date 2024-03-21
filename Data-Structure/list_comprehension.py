nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

doubledNums = [number * 2 for number in nums]

print(doubledNums)
even = [number for number in nums if number % 2 == 0]
print(even)
newList = [number * 2 if number % 2 == 0 else number * 3 for number in nums]
print(newList)