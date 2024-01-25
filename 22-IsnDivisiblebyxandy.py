# 2024 Coding Challenge
# https://www.codewars.com/kata/5545f109004975ea66000086/train/python

def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

print(is_divisible(3,2,2)) # False
print(is_divisible(3,3,4)) # False