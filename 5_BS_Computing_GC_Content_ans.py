"""
Rosalind: BS - Computing GC Content ANSWER

Problem: The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated.
"""

# === Read data from the file (FASTA formatted file)

def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

# Calculate GC Content from FASTA formatted text file:


def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round(((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)

# Storing File contents in a list
FASTAFile = readFile("5_BS_Computing_GC_Content.txt")
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

# === Format the data (Store the data in a convenient way)
# === Run needed operation on the data (pass the data to our gc_content function)

# Using Dictionary Comprehension to generate a new dictionary with GC content value
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}
# Looking for max value in values() of our new dictionary
MaxGCKey = max(RESULTDict, key=RESULTDict.get)
# === Collect results (Rosalind Submission in our case)
# Printing Rosalind formatted result
print(f'{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}')
