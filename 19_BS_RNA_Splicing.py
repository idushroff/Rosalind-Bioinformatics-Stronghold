"""
Rosalind - BS - RNA Splicing

Problem: After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset:
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output:
MVYIADKQHVASREAYGHMFKVCA
"""

# Parsing through the FASTA File without Biopython:

# sequences = []
# DNAsequence = ''
# # for parsing the FASTA file
# with open("19_BS_RNA_SplicingAD.txt") as file:
#     for line in file:
#         if line.startswith(">"):
#             nextline = str()  # this is the same as saying nextline = ""
#         else:
#             nextline += (line.strip("\n"))
#             if len(nextline) > len(DNAsequence):
#                 DNAsequence = nextline
#             if len(nextline) < len(DNAsequence):
#                 sequences.append(nextline)
#     sequences.append(DNAsequence)
#
# for elem in sequences:
#     print('elem', len(elem))
# print(sequences)
#
# DNAseq = sequences[-1]
# print('DNA1', len(DNAseq), DNAseq)
# introns = sequences[:-1]
# introns.sort(reverse=True)
# print('introns', introns)

# alternatively code for the above is:

"""The chunk of code below parses through the FASTA file and stores the DNA sequence followed by 
all the introns in a list called sequences using BioPython. Both give the same answer"""

from Bio import SeqIO

sequences = []
handle = open('19_BS_RNA_SplicingAD.txt', 'r')
for record in SeqIO.parse(handle, 'fasta'):
    sequence = []
    seq = ''
    for nt in record.seq:
        seq += nt
    sequences.append(seq)
print(len(sequences))
handle.close()

DNAseq = sequences[0]
print('DNA1', len(DNAseq), DNAseq)
introns = sequences[1:]
introns.sort(reverse=True)
print('introns', introns)


def edit_DNA(DNA):
    """This function deletes the introns and then transcribes the DNA strand into an mRNA strand."""
    for intron in introns:
        DNA = DNA.replace(intron, "")
    DNA = DNA.replace('T', 'U')
    return DNA


def RNAtoProtein(RNAsequence):
    """This function converts the transcribed mRNA strand to a protein stand."""

    codons = {"UUU": "F", "CUU": "L", "AUU": "I",
              "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I",
              "GUC": "V", "UUA": "L", "CUA": "L", "AUA": "I",
              "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M",
              "GUG": "V", "UCU": "S", "CCU": "P", "ACU": "T",
              "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T",
              "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T",
              "GCA": "A", "UCG": "S", "CCG": "P", "ACG": "T",
              "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N",
              "GAU": "D", "UAC": "Y", "CAC": "H", "AAC": "N",
              "GAC": "D", "UAA": "Stop", "CAA": "Q", "AAA": "K",
              "GAA": "E", "UAG": "Stop", "CAG": "Q", "AAG": "K",
              "GAG": "E", "UGU": "C", "CGU": "R", "AGU": "S",
              "GGU": "G", "UGC": "C", "CGC": "R", "AGC": "S",
              "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R",
              "GGA": "G", "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}

    split_RNA_seq = [RNAsequence[i:i + 3] for i in range(0, len(RNAsequence), 3)]
    print(split_RNA_seq)
    protein = ''
    for codon in split_RNA_seq:
        aminoacid = codons.get(codon)
        if aminoacid != 'Stop':
            protein += str(aminoacid)
    return protein


splicedDNA = edit_DNA(DNAseq)
print('edittedDNA2', splicedDNA)
proteinn = RNAtoProtein(splicedDNA)
print(proteinn)
