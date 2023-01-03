"""
Rosalind: BS - Counting DNA Nucleotide

Problem: A string is simply an ordered collection of symbols
selected from some alphabet and formed into a word; the length
of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains
the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective
number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

#my method
def count_nucleotides(dna_string_s):
    dna_string_s_lst = list(dna_string_s)
    counta = 0
    countt = 0
    countg = 0
    countc = 0
    for char in dna_string_s_lst:
        if char == 'A':
            counta += 1
        elif char == 'T':
            countt += 1
        elif char == 'G':
            countg += 1
        else:
            countc += 1
    return f"A: {counta}, T: {countt}, G: {countg}, C: {countc}"


s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
print(count_nucleotides(s))


# other better methods: Method 1
l = list(s) # first convert this string to a list
dictionary = {}
for letters in l:
    if letters in dictionary:
        dictionary[letters] += 1
    else:
        dictionary[letters] = 1
for key, value in dictionary.items():
    print(key, value)

# Method 2: using counter
wordcountDict: dict[str, int] = {}
from collections import Counter

wordcountDict = Counter(l)
for key, value in wordcountDict.items():
    print(key, value)