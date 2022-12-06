"""Rosalind: Enumerating Gene Orders = Permutations

Problem: A permutation of length n is an ordering of the
positive integers {1,2,…,n}. For example, π=(5,3,2,1,4)
is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n,
followed by a list of all such permutations (in any order)."""

from itertools import permutations


def permutation(n):
    var = [i+1 for i in range(n)]
    # print(var)
    permutes = [j for j in list(permutations(var))]
    # print(permutes)

    for x in iter(permutes):
        joined = ''
        # print(x)
        for j in x:
            joined += str(j)
        s = str(joined)
        # print(s)

        result = ''
        for ch in s:
            result = result + ch + ' '
        print(result[:-1])

    return len(permutes)


# print(permutation(3))
print(permutation(6))