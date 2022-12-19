"""
Rosalind: BS - Open Reading frames

Problem: Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE

PSEUDOCODE:
# Use a set since we want to return distinct protein.
# Sets keep track of distinct elements without us needing to worry about adding duplicates.
# Find for the Start codon.
# Use a new index since we'll want to return to the ith position of the strand in case there are multiple start codons in a row.
# Continue, if necessary, until we hit the end of the DNA sequence.
# Add the protein and break if we hit a Stop codon.
# Otherwise, add to the current protein.
# Convert protein from a set to list of strings to allow output to be written in the correct form more efficiently.
"""

# 1. transcribe the DNA into an RNA strand


def transcription(seq):
    return seq.replace('T', 'U')

# 2. translate the RNA strand into all possible protein sequences

def reverse_complement(DNA):
    lookup = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([lookup[c] for c in reversed(DNA)])

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

    RNA_seq1 = [RNAsequence[i:i + 3] for i in range(0, len(RNAsequence), 3)]
    # print(RNA_seq1)

    RNA_seq2 = [RNAsequence[i:i + 3] for i in range(1, len(RNAsequence), 3)]
    # print(RNA_seq2)

    RNA_seq3 = [RNAsequence[i:i + 3] for i in range(2, len(RNAsequence), 3)]
    # print(RNA_seq3)

    RNA_translated = [RNA_seq1, RNA_seq2, RNA_seq3]

    proteins = []

    for RNA_seq in RNA_translated:
        protein = ''
        for codon in RNA_seq:
            aminoacid = codons.get(codon)
            protein += str(aminoacid)
        proteins.append(protein)
    return proteins


def orfs(pp):
    for p in pp:
        if 'M' and 'Stop' in p:
            # print('yes')

            start_indexes = [index for index, char in enumerate(p) if char == 'M']
            # print('start_indexes-> ', start_indexes)

            stop_indexes = []
            for position in range(len(p)):
                if p[position:].startswith('Stop'):
                    stop_indexes.append(position) #MIGHT HAVE TO DO THE PLUS ONE TO ACCOUNT FOR THE FACT THAT PYTHON USES ZERO BASED INDEXING
            # print('stop_indexes-> ', stop_indexes)

            for i in start_indexes:
                # print(i)
                stop_index = [num for num in stop_indexes if num > i]
                # print(stop_index)
                orffffs = set()
                if len(stop_index) >= 1:
                    ORF = p[i:stop_index[0]]
                    orffffs.add(ORF)
                for line in orffffs:
                    print(line)


# sample dataset:
# DNAsequence = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

# for actual dataset:
with open("17_BS_Open_Reading_Frames.txt") as file:
    for line in file:
        if line.startswith(">"):
            nextline = str()
        else:
            nextline += (line.strip("\n"))
    DNAsequence = nextline
    print('DNASeq', DNAsequence)

# print('og DNA->', DNAsequence)


# print("mRNA strand from DNA->", transcription(DNAsequence))

RNAsequence = transcription(DNAsequence)
pp = RNAtoProtein(RNAsequence)

# print('diff possible proteins from the mRNA->', pp)

RNAseq_reverse_complement = reverse_complement(DNAsequence)
# print('Reverse Complement-> ', RNAseq_reverse_complement)
pp_1 = transcription(RNAseq_reverse_complement)
# print('mRNA from the reverse complement->', pp_1)
pp_reversed = RNAtoProtein(pp_1)

# print('diff possible proteins from the mRNA reverse complement->', pp_reversed)

# find ORFs from both strands
orfs(pp)
orfs(pp_reversed)

