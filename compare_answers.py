
# how to compare the contents of two txt files with multiple lines in python

newline = []
with open('ans1.txt') as file_1:
    for line in file_1:
        newline.append(line.strip("\n"))
    print(newline)

nextline = []
with open('ans2.txt') as file_2:
    for line in file_2:
        nextline.append(line.strip("\n"))
    print(nextline)

DF = [x for x in newline if x not in nextline]
print('ans', DF)
