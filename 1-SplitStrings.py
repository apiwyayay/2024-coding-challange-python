# 2024 Coding Challenge
# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

def solution(s):
    if len(s) % 2 == 0:
        return [s[i:i+2] for i in range(0, len(s), 2)]
    else:
        return [s[i:i+2] for i in range(0, len(s)-1, 2)] + [s[-1] + "_"]

print(solution("asdfadsf")) #['as', 'df', 'ad', 'sf']
print(solution("asdfads")) #['as', 'df', 'ad', 's_']