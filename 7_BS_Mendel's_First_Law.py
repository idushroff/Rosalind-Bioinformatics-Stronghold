"""
Rosalind: BS - Mendel's First Law

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

Hint: Consider simulating inheritance on a number of small test cases in order to check your solution
restate the problem: What is the probability that 2 organisms mate (part a) and that their offspring has a dominant phenotype (part b)?
part a of this problem can be solved using the probability tree (without replacement):
Finally, you have to multiply part a with part b and sum all the probabilities to get the required output
"""


def probability(k, m, n):
    pop = k+m+n
    prob = (4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1))/(4*pop*(pop-1))
    return round(prob, 5)


print(probability(2, 2, 2))
print(probability(27, 17, 19))



