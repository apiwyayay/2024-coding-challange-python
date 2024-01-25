# 2024 Coding Challenge
# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c/train/python

def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'


print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])) # 'found the needle at position 3'
print(find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle', 'something somebody lost a while ago'])) # 'found the needle at position 5'