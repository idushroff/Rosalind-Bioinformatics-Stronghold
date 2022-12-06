"""Rosalind: BS - Consensus and Profile

Problem: A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.

Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).

A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

See visual on Rosalind

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""


# Sample Dataset stored in file named:
# === Read data from the file (FASTA formatted file)


def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]


# Storing File contents in a list
FASTAFile = readFile("20_BS_Consensus_and_Profile")
# Dictionary for Labels + Data
FASTADict = {}
# String for holding the current label
FASTALabel = ""

# === Clean/Prepare the data (Format for ease of you with our gc_content function)
# Converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

print('FASTADict ->', FASTADict)

# Using Dictionary Comprehension to generate a list of all the dna sequences
resulting_data = list(FASTADict.values())
print('resulting data ->', resulting_data)

# creating a new dictionary which keeps the count of each nucleotide at each position of the DNA string

n = len(resulting_data[0])

profile_matrix = {
    'A': [0] * n,
    'T': [0] * n,
    'G': [0] * n,
    'C': [0] * n,
    }

for seq in resulting_data:
    for position, nucleotide in enumerate(seq):
        # print(position, nucleotide)
        profile_matrix[nucleotide][position] += 1
print(profile_matrix)

# using the profile matrix to construct a consensus string
consensus = [] # list to save the nucleotide with max count from each row
# so note you are looking at the matrix after rotating it 90 degrees

for position in range(n):
    max_count = 0
    max_nucleotide = None
    for nucleotide in ['A', 'C', 'G', 'T']:
        count = profile_matrix[nucleotide][position]
        if count > max_count:
            max_count = count
            max_nucleotide = nucleotide
    consensus.append(max_nucleotide)

consensus_string = ''.join(consensus)
print(consensus_string)

