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


sequences = []
# for parsing the FASTA file
with open("19_BS_RNA_Splicing.txt") as file:
    for line in file:
        if line.startswith(">"):
            nextline = str()
        else:
            nextline += (line.strip("\n"))
            # print(nextline)
            sequences.append(nextline)


DNAseq = sequences[0]
introns = sequences[1:]
print(DNAseq)
print(introns)


def transcription(seq):
    return seq.replace('T', 'U')


def edit_DNA(DNA):
    for intron in introns:
        if intron in DNA:
            print('DNA', DNA)
            a = DNA.split(intron)
            print('a', a)
            new_DNA_seq = ''
            for bit in a:
                new_DNA_seq += bit
            print('edittedDNA', new_DNA_seq)
        DNA = new_DNA_seq #I think problem is here somewhere
    return DNA


def RNAtoProtein(RNAsequence):
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


print('final editted dna', edit_DNA(DNAseq))
transcribed = transcription(DNAseq)
print('transcribed DNA', transcribed)
proteinn = RNAtoProtein(transcribed)
print(proteinn)






