# Rosalind - Bioinformatics Stronghold
# 2. Transcribing DNA into RNA

"""
Problem
An RNA string is a string formed from the alphabet containing
'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand,
its transcribed RNA string u is formed by replacing all
occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
"""

#my method:
t = 'GATGGAACTTGACTACGTAAATT'
u = t.replace('T', 'U')
print(u)

# Method 2


def transcription(seq):
    return seq.replace('T', 'U')


print(transcription("GATGGAACTTGACTACGTAAATT"))
