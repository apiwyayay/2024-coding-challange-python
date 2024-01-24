# 2024 Coding Challenge
# https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python

def solution(string):
    return string[::-1]

print(solution("world")) # 'dlrow'
print(solution("hello")) # 'olleh'
print(solution("")) # ''
print(solution("h")) # 'h'