"""
Rosalind - BS - Locating Restriction Sites

Problem: A DNA string is a reverse palindrome if it is equal to its reverse complement.
For instance, GCATGC is a reverse palindrome because its reverse complement
is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string
having length between 4 and 12. You may return these pairs in any order.

Sample Dataset:
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output:
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4

"""

# for parsing the FASTA file
with open("18_BS_Locating_Restriction_Sites.txt") as file:
    for line in file:
        if line.startswith(">"):
            nextline = str()
        else:
            nextline += (line.strip("\n"))
    DNAsequence = nextline
    print('DNASeq', DNAsequence)


def reverse_complement(DNA):
    lookup = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([lookup[c] for c in reversed(DNA)])

# REVcom = reverse_complement(DNAsequence)

# print('REVCom', reverse_complement(DNAsequence))

# NOTE: They are using index starting from 1 not zero

# take a chunk of dna starting from start of the dna
# of the len of 4 then 5 6
# so we have will have two loops
# etc up until 12 and see if it equals to its reverse palindrome
# if yes then rerun the index posistion of where the first character of this chunk starts

l = 4
answers = []
while l <= 12:
    for char in enumerate(DNAsequence):
        # print(char)
        starting_index = char[0]

        # print(starting_index)
        ending_index = starting_index + l
        chunk = DNAsequence[starting_index:ending_index]
        if len(chunk) == l:
            print(starting_index, chunk, len(chunk))
            revcom = reverse_complement(chunk)
            # print(revcom)
            if chunk == revcom:
                # print('hi', chunk, starting_index, len(chunk))
                answers.append((starting_index+1, len(chunk), chunk))
    l += 1
    # return starting_index len(chunk)
print(answers)

for ans in sorted(answers):
    print(ans[0], ans[1])


