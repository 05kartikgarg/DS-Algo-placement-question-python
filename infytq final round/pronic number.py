pronic=[]
for i in range(1,1000):
    pronic.append(i*(i+1))

s=input()
my_set=set()
for i in range(len(s)):
    string=''
    for j in range(i,len(s)):
        string+=s[j]
        if int(string) in pronic:
            my_set.add(int(string))
my_set=sorted(list(my_set))

if len(my_set)!=0:
    for i in range(len(my_set)-1):
        print(my_set[i],end=',')
    print(my_set[len(my_set)-1])
else:
    print(-1)

'''
input: 93012562
output: 2,6,12,30,56,930

input: 12345
output: 2,12

'''