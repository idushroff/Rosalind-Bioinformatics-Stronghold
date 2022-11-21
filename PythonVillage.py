# Rosalind Python Village
# Variables and some Arithmetic
from typing import Dict

a = 3
b = 5
print(f'{a}^2+ {b}^2 = {a ** 2 + b ** 2}')

a = 959
b = 963
print(f'{a}^2+ {b}^2 = {a ** 2 + b ** 2}')

# Strings and Lists
a = 22
b = 27
c = 97
d = 102
s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"
print(f'{s[a:b + 1]} {s[c:d + 1]}')

# it also works if I manually up the value of b + d
b = 28
d = 103
print(f'{s[a:b]} {s[c:d]}')

s = "osHVpq7Yp1F03Grampus1vGhz2b5WCUug8Yj7j6cepedianaAv8tcjXBi4o49ejdcko7JuMXtPR10n5BwnwMAVKxDKfzQRcN8YwjlkQUlclEI3lA0lVhBr5bHrBrR2Xbv6R4boH921fse15Mf87aPRc8A8F7UvbOzOWiqKtTNz4S"
a = 13
b = 19
c = 39
d = 47
print(f'{s[a:b + 1]} {s[c:d + 1]}')

# Rosalind Python Village: Conditions and Loops
# Two positive integers a<b<10000. The sum of all odd integers from a through b inclusively.
a = 100
b = 200
result = 0
for x in range(a, b + 1):
    if x % 2 != 0:
        result += x
print(result)

"""i+=1 is the same as i=1+1
1== is the same as i = (+1)
x % 2 is the same as x divided by 2
!= is the same as not equal to"""

# Rosalind Python Village Task 5: Working with files
"""you are given a file containing at most 1000 lines.
Return a file containing all the even-numbered lines from the original file.
Assume 1-based numbering of lines"""
# pos = position

# outputFile = []
#
# with open('C:/Users/IRIS/PycharmProjects/pythonProject1/input.txt', 'r') as f:
#     outputFile = [line for pos, line in enumerate(f.readlines()) if pos % 2 != 0]
# print(outputFile)
# with open('C:/Users/IRIS/PycharmProjects/pythonProject1/output.txt', 'w') as f:
#     f.write(''.join([line for line in outputFile]))

# Rosalind Python Village Task 6: Dictionaries
""" Problem: Given: A string s of length at most 10000 letters. 
Return: The number of occurrences of each word in s, 
where words are separated by spaces. Words are case-sensitive, 
and the lines in the output can be in any order."""

# Method 1: using for loop (Generic approach)
s = "We tried list and we tried dicts also we tried Zen"
print(s.split(' '))

wordcountDict: dict[str, int] = {}
for word in s.split(' '):
    if word in wordcountDict:
        wordcountDict[word] += 1
    else:
        wordcountDict[word] = 1
for key, value in wordcountDict.items():
    print(key, value)

# Method 2: collections counter (Optimized pythonic approach, using collections module:)

from collections import Counter

wordcountDict = Counter(s.split(' '))

for key, value in wordcountDict.items():
    print(key, value)

# A dictionary is made up of items =>keys = words and values =
