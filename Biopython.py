"""
Biopython is a set of freely available tools for
biological computation written in Python by an
international team of developers.

This document has useful biopython commands with examples.

https://www.youtube.com/watch?v=ocA2IMe7dpA&list=TLPQMDcwMTIwMjP4ausuQTa0Jw&index=2

0:00:42 SeqIO module: reading and parsing sequence files (FASTA/FASTQ)
0:03:28 Calculating GC content of sequence which is read with Biopython SeqIO module from FASTA file
0:06:17 Biopython Seq object with example of central dogma - translation and transcription
0:09:38 Checking quality of reads - reading/parsing FASTQ file
0:14:52 NCBI databases: Accessing via Biopython Entrez
0:21:12 Pairwise sequence alignment with pairwise2 module
0:31:07 Using BLAST with Biopython to align sequences
0:34:31 COVID-19 genome analysis
0:44:48 Motif objects creation in Biopython
0:49:25 Plotting sequences information: length & GC content
0:52:10 Faster reads of big sequence files with index functionality
0:58:07 Filtering sequence files
"""

from Bio.Seq import Seq
sequence = Seq("AGTACAGAGSG")
print(sequence)


# count() - The Seq object has a .count() method, just like a string.
# Note that this gives a non-overlapping count
sequence = Seq("AAAA")
print(sequence.count("AA"))

# overlapping count
print(sequence.count_overlap("AA"))

# calculate GC content
from Bio.SeqUtils import GC
sequence = Seq("ATGCATGAGTACGATCAGTAGATA")
print('GC content', GC(sequence))

"""
To get template strand from coding strand
(template strand if is the complement of coding strand)
"""
# use reverse complement method
coding_dna = Seq("ATGCATGAGTACGATCAGTAGATA")
template_dna = coding_dna.reverse_complement()
print('template strand', template_dna)


"""
Transcription = replacing T with U in the 
coding Strand of the DNA (which goes from 5' to 3' end).
"""
# use transcribe method
messenger_rna = coding_dna.transcribe()
print('messenger_rna', messenger_rna)

# The Seq object also includes a back-transcription method for
# going from the mRNA to the coding strand of the DNA
coding_strand = messenger_rna.back_transcribe()
print('coding strand', coding_strand)


# for translating RNA to protein - from mRNA strand
print('protein', messenger_rna.translate())

# for translating RNA to protein - directly from the coding strand
print('protein', coding_dna.translate())


"""0:09:38 Checking quality of reads - reading/parsing FASTQ file"""
#  see jupyter notebook
