# """
# Rosalind: BS -
#
# """
#
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
# # print(sequences)


# a = "-"
# b = a.join(("MCO", "MCO"))
# c = a.join("MCO")
# # d = a.join("MCO", "MCO") # this one gives error
#
# print(b)
# print(c)
# print(d)


