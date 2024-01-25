# 2024 Coding Challenge
# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python

def century(year):
    return (year + 99) // 100

print(century(1705)) # 18
print(century(1900)) # 19
print(century(1601)) # 17
print(century(2000)) # 20