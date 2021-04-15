from itertools import permutations
elements=input().split()
permutation_tuples=permutations(elements)
l1=[]
for i in permutation_tuples:
    val=int(''.join(i))
    l1.append(val)
print(max(l1))
