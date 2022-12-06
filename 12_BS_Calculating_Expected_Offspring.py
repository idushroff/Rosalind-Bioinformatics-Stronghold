"""
Rosalind - BS - Calculating Expected Offspring

Problem: For a random variable X taking integer values between 1 and n, the expected value of X is E(X)=∑nk=1k×Pr(X=k). The expected value offers us a way of taking the long-term average of a random variable over a large number of trials.

As a motivating example, let X be the number on a six-sided die. Over a large number of rolls, we should expect to obtain an average of 3.5 on the die (even though it's not possible to roll a 3.5). The formula for expected value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5.

More generally, a random variable for which every one of a number of equally spaced outcomes has the same probability is called a uniform random variable (in the die example, this "equal spacing" is equal to 1). We can generalize our die example to find that if X is a uniform random variable with minimum possible value a and maximum possible value b, then E(X)=a+b2. You may also wish to verify that for the dice example, if Y is the random variable associated with the outcome of a second die roll, then E(X+Y)=7.

Given: Six non-negative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
"""

from __future__ import division
import sys

# pop = population
# the *2 because we have to account for two offspring by each couple
# prd = the probablity of dominant phenotype expressed by the offspring


sd1 = {'AA-AA': {"pop": 2, "prd": (4 / 4)},
       'AA-Aa': {'pop': 0, 'prd': (4 / 4)},
       'AA-aa': {'pop': 0, 'prd': (4 / 4)},
       'Aa-Aa': {'pop': 2, 'prd': (3 / 4)},
       'Aa-aa': {'pop': 0, 'prd': (2 / 4)},
       'aa-aa': {'pop': 2, 'prd': (0 / 4)}}

sd2 = {'AA-AA': {'pop': (16302 * 2), 'prd': (4 / 4)},
       'AA-Aa': {'pop': (17878 * 2), 'prd': (4 / 4)},
       'AA-aa': {'pop': (16276 * 2), 'prd': (4 / 4)},
       'Aa-Aa': {'pop': (17584 * 2), 'prd': (3 / 4)},
       'Aa-aa': {'pop': (2 * 19292), 'prd': (2 / 4)},
       'aa-aa': {'pop': (2 * 17228), 'prd': (0 / 4)}}

sd3 = {'AA-AA': {'pop': (17532 * 2), 'prd': (4 / 4)},
       'AA-Aa': {'pop': (19719 * 2), 'prd': (4 / 4)},
       'AA-aa': {'pop': (16154 * 2), 'prd': (4 / 4)},
       'Aa-Aa': {'pop': (19580 * 2), 'prd': (3 / 4)},
       'Aa-aa': {'pop': (2 * 16817), 'prd': (2 / 4)},
       'aa-aa': {'pop': (2 * 16379), 'prd': (0 / 4)}}

#  for sd1:
pr = []
for key in sd1:
    pr.append(sd1[key].get('pop') * sd1[key].get('prd'))
print(pr)

total = 0.0
for item in pr:
    total += item
print(total)

# for sd2:
pr = []
for key in sd2:
    pr.append(sd2[key].get('pop') * sd2[key].get('prd'))
print(pr)

total = 0.0
for item in pr:
    total += item
print(total)

# for sd3:
pr = []
for key in sd3:
    pr.append(sd3[key].get('pop') * sd3[key].get('prd'))
print(pr)

total = 0.0
for item in pr:
    total += item
print(total)

# another method I found online:
# first we have to import sys and divison (done above)
# then run this code on the command line


def main():
    dominance = {'AA_AA': 1,
                 'AA_Aa': 1,
                 'AA_aa': 1,
                 'Aa_Aa': (3/4),
                 'Aa_aa': (2/4),
                 'aa_aa': 0}

    population = {'AA_AA': sys.argv[1],
                  'AA_Aa': sys.argv[2],
                  'AA_aa': sys.argv[3],
                  'Aa_Aa': sys.argv[4],
                  'Aa_aa': sys.argv[5],
                  'aa_aa': sys.argv[6]}

    offspring = 0

    for d in dominance:
        offspring += dominance[d] * float(population[d])

    # each couple produces 2 offsprings
    print(offspring * 2)


if __name__ == "__main__":
    main()
