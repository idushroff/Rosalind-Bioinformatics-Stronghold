"""Rosalind: BS - Overlap Graphs

Problem: A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

# Sample Dataset stored in file named:
# === Read data from the file (FASTA formatted file)


def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]


# Storing File contents in a list
FASTAFile = readFile("10_BS_Overlap_Graphs.txt")
# Dictionary for Labels + Data
FASTADict = {}
# String for holding the current label
FASTALabel = ""

# === Clean/Prepare the data (Format for ease of you with our gc_content function)
# Converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line[1:]
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

print('FASTADict ->', FASTADict)


def is_k_overlap(s1, s2, k):
    return s1[-k:] == s2[:k]


import itertools


def k_edges(data, k):
    edges = []
    for u, v in itertools.combinations(data, 2):
        u_dna, v_dna = data[u], data[v]

        if is_k_overlap(u_dna, v_dna, k):
            edges.append((u, v))

        if is_k_overlap(v_dna, u_dna, k):
            edges.append((v, u))
    return edges


for tupp in k_edges(FASTADict, 3):
    print(tupp[0], tupp[1])
