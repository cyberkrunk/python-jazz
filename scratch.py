listA = [0, 4, 7, 11]
trans = 60
listB = [a + trans for a in listA]

print(listB)

print('----------')



listA = [1, 2, 3, 4]
listB = [1, 1, 1, 1]

listC = [a + b for a, b in zip(listA, listB)]

listE = [1]

print(listC)

listD = [sum(x) for x in zip(listA, listE)]

print(listD)

exp2 = []
exp3 = []
exp5 = []

exp2 = [2**x for x in range(17)]
exp3 = [3**y for y in range(13)]
exp5 = [5**z for z in range(13)]

print(exp2)

print()

print(exp3)

print()

print(exp5)

print()

Blerg = list(range(100))
print(Blerg)

