"""
Rosalind: Longest Increasing Subsequence

Note: there is a difference b/w longest increasing subsequence vs longest non-decreasing subsequence.
For eg: if you have the seq [-1, 3, 4, 5, 2, 2, 2]
the longest increasing subseq = [-1, 3, 4, 5]
the longest non-decreasing subseq = [-1, 2, 2, 2]

Problem: A subsequence of a permutation is a collection of elements of the permutation
in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing
if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9),
an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3).
You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

Sample Dataset
5
5 1 4 2 3

Sample Output
1 2 3
5 4 2

Note: This is a dynamic programming problem.


Sample Dataset 2
9
8, 2, 1, 6, 5, 7, 4, 3, 9


Sample Output
2, 6, 7, 9
8, 6, 5, 4, 3


"""

with open("21_BS_Longest_Increasing_Subsequence.txt") as file:
    contents = file.readlines()
    print(contents)

    n = contents[0]
    print(n)

    seq = ''.join(contents[1:]).replace('\n', ' ')
    print('seq', seq)

nospace_seq = seq.replace(' ', '')
inc_subseqss = []
inc_subseq = []
# decreasing_subseq = []
#
#
for i in nospace_seq:
    print('i----', i)
    i = int(i)
    inc_subseq.append(i)
    print(inc_subseq)

    for j in nospace_seq:
        print('j', j)
        j = int(j)
        if j > i:
            inc_subseq.append(j)
print(inc_subseq)


#     # elem = int(elem)
#     if len(increasing_subseq) == 0:
#         increasing_subseq[0] = max(nospace_seq)
#
#     elif elem > nospace_seq[0]:
#         increasing_subseq += elem
#
#
# for elem in nospace_seq:
#     if elem == nospace_seq[0]:
#         decreasing_subseq += elem
#     elif elem < nospace_seq[0]:
#         decreasing_subseq += elem
#     # prev_elem = elem
#     # print(prev_elem)
#     # if elem > prev_elem:
#     #     increasing_subseq += elem
#     # elif elem < prev_elem:
#     #     decreasing_subseq += elem
#
# print(increasing_subseq)
# print(decreasing_subseq)
