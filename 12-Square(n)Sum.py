# 2024 Coding Challenge
# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python

def square_sum(numbers):
    return sum(i**2 for i in numbers)

print(square_sum([1, 2])) # 5
print(square_sum([0, 3, 4, 5])) # 50
print(square_sum([])) # 0