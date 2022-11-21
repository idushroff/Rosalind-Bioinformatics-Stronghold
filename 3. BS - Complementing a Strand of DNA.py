# Rosalind - Bioinformatics Stronghold
# 3. Complementing a Strand of DNA


"""
Problem
In DNA strings, symbols 'A' and 'T' are complements of each other,
as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed
by reversing the symbols of s, then taking the complement of each
symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s. """


# my method:
def ReverseComplement(seq):
    DNA_ReverseComplement = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    sc = "".join([DNA_ReverseComplement.get() for c in text])
    return reversed(sc)


print(ReverseComplement("AAAACCCGGT"))

# https://www.youtube.com/watch?v=G8-fNk9vlaY&t=16s

# drawing inspo from this code:
# def g(text):
#     replacements = {"&": "\&", "#": "\#"}
#     text = "".join([replacements.get(c, c) for c in text])