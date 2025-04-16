"""
Rosalind - BS - Finding a protein Motif

Problem: To allow for the presence of its varying forms, a protein motif is
represented by a shorthand as follows: [XY] means "either X or Y" and {X}
means "any amino acid except X." For example, the N-glycosylation motif is
written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein
 by its access ID "uniprot_id" in the UniProt database, by inserting the
 ID number into

http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at
http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output
its given access ID followed by a list of locations in the protein string
where the motif can be found.

Sample dataset:
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output:
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

# We have to use the requests python library
# for this problem as it will allow us to fetch the fasta files from Uniprot.

import requests as r
from Bio import SeqIO
from io import StringIO

# read the uniprot_IDs from the sample data set

lst_of_IDs = []
sample_dataset = open('16_BS_Finding_a_protein_motif.txt', 'r')

uniprot_ids = [line.rstrip() for line in sample_dataset.readlines()]
# print(uniprot_ids, end='\n')


# Acquire the fasta files for each uniprot_ID
sequences = {}
for id in uniprot_ids:
    baseURL = 'http://www.uniprot.org/uniprot/'
    currentURL = baseURL + id[:6] + '.fasta'
    # print(id[:6])
    # print('1. URL', currentURL)
    response = r.get(currentURL)
    # print('2.', response)
    sequences[id] = (response.text.split('\n'))
    sequences[id] = ''.join(sequences[id][1::])

    # Seq = StringIO(Data)
    # sequences = ''.join(Seq)
    #
    # pSeq = list(SeqIO.parse(Seq, 'fasta'))
    #
    # print('3.', Data)
    # print('4.', pSeq)
    # print('5.', sequences)

# function to find the N-glycosylation motif


def N_glycos_motif(ID, sequence):
    # print(ID)
    # print(sequence)
    sequence = list(sequence)       #list so we can index
    global locations
    locations = []
    for i in range(0, len(sequence)-3):
        seq = sequence[i:i+4]
        if (seq[0] == 'N') and (seq[2] == 'S' or seq[2] == 'T') and (seq[1] != 'P' and seq[3] != 'P'):
            locations.append(i+1)
            # print(seq)

# print output


for key, value in sequences.items():
    N_glycos_motif(key, value)
    if not locations:
        continue
    else:
        print(key)
        print(*locations)

sample_dataset.close()


# can use this link to doublecheck my ans
# https://prosite.expasy.org/cgi-bin/prosite/ScanView.cgi?scanfile=72138585056.scan.gz&sig=N{P}[ST]{P}