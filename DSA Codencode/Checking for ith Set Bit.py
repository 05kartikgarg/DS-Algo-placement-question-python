#checking if the ith bit is set bit or not(in the binary representation of n)
# set bit means it is 1

def checkibit(n,i):
    f=1
    f=f<<i

    res=int(n & f)
    if res==0:
        print("False")
    else:
        print("True")
checkibit(32,5)

#count the total number of set bits

def countsetbit(n):
    cnt=0
    while n>0:
        if (n & 1)>0:
            cnt+=1
        n=n>>1
    print(cnt)
countsetbit(5) 
