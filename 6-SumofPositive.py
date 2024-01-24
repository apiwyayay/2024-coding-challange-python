# 2024 Coding Challenge
# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

print(positive_sum([1,2,3,4,5])) # 15
print(positive_sum([1,-2,3,4,5])) # 13
print(positive_sum([-1,2,3,4,-5])) # 9