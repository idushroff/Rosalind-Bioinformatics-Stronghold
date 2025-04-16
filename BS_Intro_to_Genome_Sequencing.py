"""
Rosalind - BS - Intro to Genome Sequencing

Problem: For a collection of strings, a larger string containing every one of the smaller strings as a substring is
called a superstring.
By the assumption of parsimony, a shortest possible superstring over a collection of reads serves
as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent
reads deriving from the same strand of a single linear chromosome).
The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire
chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).

Sample Dataset
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC

Sample Output
ATTAGACCTGCCGGAATAC

Note: Although the goal of fragment assembly is to produce an entire genome, in practice it is only possible to
construct several contiguous portions of each chromosome, called contigs. Furthermore, the assumption made above
that reads all derive from the same strand is also practically unrealistic; in reality, researchers will not know
the strand of DNA from which a given read has been sequenced.
"""

# parse through the given dataset (i.e. FASTA file)

from Bio import SeqIO

sequences = []
file = open('BS_Intro_to_Genome_Sequencing.txt', 'r')
for record in SeqIO.parse(file, 'fasta'):
    seq = ''
    for nucleotide in record.seq:
        seq += nucleotide
    sequences.append(seq)
print(sequences)

# Gluing together pairs of reads that overlap by more than half their length = 25+ nucleotides
for read in sequences:
    if

