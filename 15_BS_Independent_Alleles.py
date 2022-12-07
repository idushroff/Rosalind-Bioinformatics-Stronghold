"""
The purpose of this problem: Pitfalls of Reversing Translation
When researchers discover a new protein, they would like to infer the strand of mRNA from which
this protein could have been translated, thus allowing them to locate genes associated with this
protein on the genome.

Unfortunately, although any RNA string can be translated into a unique protein string, reversing
the process yields a huge number of possible RNA strings from a single protein string because most
amino acids correspond to multiple RNA codons (see the RNA Codon Table).

Because of memory considerations, most data formats that are built into languages have upper
bounds on how large an integer can be: in some versions of Python, an "int" variable may be
required to be no larger than 231−1, or 2,147,483,647. As a result, to deal with very large
numbers in Rosalind, we need to devise a system that allows us to manipulate large numbers
without actually having to store large numbers.
"""

"""
Rosalind: BS - Independent Alleles

Problem: For positive integers a and n, a modulo n (written a mod n in shorthand) is the 
remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.

Modular arithmetic is the study of addition, subtraction, multiplication, and division with 
respect to the modulo operation. 
We say that a and b are congruent modulo n if a mod n= b mod n; 
in this case, we use the notation a ≡ b mod n.

Two useful facts in modular arithmetic are that if a≡b mod n and c≡d mod n, 
then a+c ≡ b+d mod n and a×c ≡ b×d mod n. 
To check your understanding of these rules, you may wish to verify these 
relationships for a=29, b=73, c=10, d=32, and n=11.

As you will see in this exercise, some Rosalind problems will ask for a (very large) 
integer solution modulo a smaller number to avoid the computational pitfalls that arise
with storing such large numbers.

Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been 
translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset: MA
Sample Output: 12

Hint: What does it mean intuitively to take a number modulo 1,000,000?

Note: The mod % operator returns the remainder of dividing two numbers.
"""

from math import factorial


a = 29
b = 73
c = 10
d = 32
n = 11

h = (a + c) % n
g = (b + d) % n

print(h == g)

j = (a * c) % n
k = (b * d) % n

print(k == j)

# these are the no of possible codons that this protein might have come from:

# M: 1, A: 4,

# Therefore, this means that there 1 * 4 combinations that could have resulted in the protein sequence MA

# sd = list('MTCIYTFIFCVNPIKGCSHHGVVMFCGTVYHMIIVLRSLQRCFLPIQCTHRVARSVQFVCQKVMEHKMWSRSHCTDQCVMKPSDCRMRWWADDRRHTTQERIEENALGYQDHHICFMLQALNRFFRAEVKYGWNGQQCLMTAKKTLPPIESKRELRNIFGNVSLFWVFTRYFITYPVWKCWIGARKWVNDHSNTYPTAKDIEMVQAGHSRMPDMPWTIGRENQMALIPTCVNGFNSLMYDPLPEQMKCWDMRRHSRKRCREYDYTKVLFLQVLDGIEYILSHFSHSWAPGMTDICYYSMAIRANARNNMKPVAGYERMKSHTPPQEEWCRLPHMSGHIYFNNWQCDDQYIWMLDEAWLLQYACDAHGKKQAKWYSNTGLQKWHKCNFSKMRCPEPTSMLSCSSWQWLFHMNHKDDRVMFFQRVWEQHELTHCYTNGHTEMHNGDVHTWAFWLNFRGFYIACRFETDLEYWWKQAIGEHTTPPIRQKYTAASRKKIKWPMLILNSKAHQQSWPAHQLKWNTQSEDNFWRMSVVEGGSFMKICMDMVTACHWESMNWHWHYAIMKLALYPWYSSAHKKICPIQSKQRDAQHVIAEWIEVFQDGQGSRMHFPSDYQWRAYAIHTRAHKLVSLIVIFAHTICIQTGVVHQVKADFFNVVQTTALLHPATPVSGVHGNDNPNQGWDLVHKMTNNFCMMVLHKSRCGHFWFGFMQQMIAFWTALSYQIPRDLFWNMPWHWTYSRTAHAYYVDRDTVGLVSSQPPVKWTYEQTIRNHMVRPYVKRVKGVYPEDQQCLHIVMSDWVPHYRQKHVYWVNNWRAHRDSCCTWIFIKAKWYRHWDMWGWQLAKAWLCKTWNEPSAACSKPKYSHSLWDLPDKEMPIYRMANKKMCLEKVGSVQGTHVEDKRVCIRRSTKCRIDEIHSQWRRMASGAKQCGRPRGRIRPKWYWLPQYVSPEADDQKILRNDAKEADVFWMEMLEYACIKLKAGADRMLMQMQIFMGWYKHTF')
sd = list('MAMA')
print(len(sd))

sde = []
for elem in sd:
    sde.append(elem)

# before every start codon there should be a stop codon, so we have to account for this
count = 0

for aa in sd:
    if aa == 'M':
        count += 1
        sde.append('STOP')
print('c', count)

print(len(sde))
print(len(sde) - len(sd)) # this is just to check if the right no of stop codons have been added

CodonTable = {'F': 2, 'L': 2, 'I': 3, 'M': 1, 'V': 4,
              'S': 6, 'P': 4, 'T': 4, 'A': 4, 'Y': 2,
              'STOP': 3,
              'H': 2, 'Q': 2, 'N': 2, 'K': 2, 'D': 2,
              'E': 2, 'C': 2, 'W': 1, 'R': 6, 'G': 4}

ha = []  # all the possible num of codon's this aa might have come from
# the 3 is accounting for the stop codon

for aa in sde:
    ha.append(CodonTable.get(aa))
print(ha)

# total num of possible RNA sequences this protein could have come from

total = 1
for num in ha:
    total *= num
    # print(total)

print(total % 1000000)

