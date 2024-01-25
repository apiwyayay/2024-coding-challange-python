# 2024 Coding Challenge
# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

def digitize(n):
    return [int(i) for i in str(n)][::-1]

print(digitize(35231)) # [1,3,2,5,3]
print(digitize(0)) # [0]
print(digitize(23582357)) # [7,5,3,2,8,5,3,2]
print(digitize(984764738)) # [8,3,7,4,6,7,4,8,9]