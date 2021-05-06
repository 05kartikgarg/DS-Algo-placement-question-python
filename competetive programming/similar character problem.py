'''
#method 1: O(n^2)
n=int(input())
s=input().lower()
q=int(input())
r=[]
for i in range(q):
    p=int(input())
    letter=s[p-1]
    c=0
    for x in range(p-1):
        if s[x]==letter:
            c+=1
    
    r.append(c)
for z in r:
    print(z)
        
'''
#method 2: O(n)

n=int(input())
s=input().lower()
q=int(input())
r=[]
for i in range(q):
    p=int(input())
    r.append(s[:p-1].count(s[p-1]))
for z in r:
    print(z)
        
