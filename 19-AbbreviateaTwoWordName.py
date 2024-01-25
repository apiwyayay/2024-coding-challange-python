# 2024 Coding Challenge
# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

def abbrev_name(name):
    return ".".join(word[0].upper() for word in name.split())

print(abbrev_name("Sam Harris")) # "S.H"
print(abbrev_name("patrick feenan")) # "P.F"
print(abbrev_name("Evan C")) # "E.V"