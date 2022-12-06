"""
Rosalind: BS - Finding a Shared Motif

Problem:A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

"""
#
#
# # === Read data from the file (FASTA formatted file)
#
#
# def readFile(filePath):
#     """Reading a file and returning a list of lines"""
#     with open(filePath, 'r') as f:
#         return [l.strip() for l in f.readlines()]
#
#
# # Storing File contents in a list
# FASTAFile = readFile("13_BS_Finding_a_Shared_Motif")
#
# # FASTAFile = readFile("5. BS - Computing_GC_Content")
#
# # Dictionary for Labels + Data
# FASTADict = {}
# # String for holding the current label
# FASTALabel = ""
#
# # === Clean/Prepare the data (Format for ease of you with our gc_content function)
# # Converting FASTA/List file data into a dictionary
# for line in FASTAFile:
#     if '>' in line:
#         FASTALabel = line[1:]
#         FASTADict[FASTALabel] = ""
#     else:
#         FASTADict[FASTALabel] += line
#
# # Using Dictionary Comprehension to generate a new dictionary
# RESULTDict = {key: value for (key, value) in FASTADict.items()}
# print('resultdict', RESULTDict)
#
#
# for value in FASTADict.values():
#     for position in range(len(value)):
#         if value[position:] == value.next[position:]:
#             print(position:)
#     print(value)

    # if [value:].startswith():

# from 9. finding a motif
# actual dataset:
# s = 'ATACCCCGGTACCCCGCTCCTACCCCGTCTAACTACCCCGGTAACTTTACCCCGATACCCCGAGTACTACCCCGAAGTACCCCGTACCCCGGCGTACCCCGCAGTTACCCCGTTAGTACCCCGATTACCCCGGTCTGGCCTACCCCGTACCCCGTACCCCGACCCTACCCCGCCCTACCCCGTGTATACCCCGATGATTTACCCCGGACCTACCCCGGGTCGATACCCCGCTACCCCGGTACCCCGATACCCCGTATCGCTACCCCGTTACCCCGAAGCCGTACCCCGATACCCCGTACCCCGGCTTGGTACCCCGCTACCCCGTTACCCCGTACCCCGCGACTTACCCCGCCATACCCCGTACCCCGGGCAATACCCCGAGCTCATTACCCCGATACCCCGTAATACCCCGTCGGATACCCCGGTGATACCCCGTACCCCGATTACCCCGTACCCCGTACCCCGTACCCCGGTAATCTAGTACCCCGCATACCCCGCCCGTTTACCCCGGCCTACCCCGTTCGTTTACCCCGTACCCCGATCGTACCCCGGACGGAGGTACCCCGTGAATACCCCGCTACCCCGTGAGATACCCCGCGTACCCCGAGTATTACCCCGGACATCCGATACCCCGTACCCCGCTATAGGTTACCCCGGTTACCCCGCTTTACCCCGTACCCCGGGGTAACTACCCCGGTCCCAATACCCCGTACCCCGATATAGAACATACCCCGGGCCGCTCTGGTTACCCCGTACCCCGTACCCCGGATACCCCGTAAGCAGTTTTTAGTACCCCGTACCCCGCGTACCCCGATACCCCGTGTTTACCCCGTACCCCGTACCCCGATTCCC'
# t = 'TACCCCGTA'
#
# for position in range(len(s)):
#     if s[position:].startswith(t):
#         print(position + 1, end=' ')
    # the plus one is becuase we have to remember that python uses 0 based indexing


# code found online to extract all the DNA sequences from the FASTA file in a list:

from Bio import SeqIO

s = []
handle = open('13_BS_Finding_a_Shared_Motif', 'r')
for record in SeqIO.parse(handle, 'fasta'):
    sequence = []
    seq = ''
    for nt in record.seq:
        seq += nt
    s.append(seq)
# print(s)
handle.close()

for i in range(len(s)):
    s[i] = s[i].replace("\n", '')
    while s[i][0] not in "ACGT":
        s[i] = s[i][1:]

# ^^^^^^^^^^^^^ all of that to format in FAST in array

# Get shortest of DNA strings
index = s.index(min(s, key=len))
# print(index)

motif = 'A'
shortest = s[index]

# Cycle over the DNA string letters
for i in range(len(shortest)):
    n = 0
    present = True
    while present:
             # Cycle inside over all other DNA strings and if it's present in there considered a motif and length gets increased by 1
        for each in s:
            if shortest[i:i+n] not in each or n>1000:
                present = False
                break
        if present:
            motif = max(shortest[i:i+n], motif, key=len)
        n += 1

print(motif)