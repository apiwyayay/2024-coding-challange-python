# 2024 Coding Challenge
# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def digital_root(n):
    if n < 10:
        return n
    else:
        return digital_root(sum(int(i) for i in str(n)))

print(digital_root(16)) #7
print(digital_root(942)) #6
print(digital_root(132189)) #6
print(digital_root(493193)) #2