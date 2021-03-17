'''
#chef and patients
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    temp=sorted(a)
    time=1
    r=[0]*n
    for i in range(len(temp)-1,-1,-1):
        ind=a.index(temp[i])
        r[ind]=time
        time+=1
        a[ind]=-1
    for i in r:
        print(i,end=' ')
    print()
  
'''

for i in range(int(input())):
    n=int(input())
    a=''
    b=''
    binary=bin(n)[2:]
    #print(binary)
    for i in range(len(binary)):
        if binary[i]=='1':
            a+='1'
            b+='0'
            #print(a,b)
            break
    for j in range(i+1,len(binary)):
        if binary[j]=='1':
            a+='0'
            b+='1'
            #print(a,b)
        else:
            a+='1'
            b+='1'
            #print(a,b)
    print(int(a,2),int(b,2))






    














    
