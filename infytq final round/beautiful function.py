num=input()
total=0

i=len(num)-1
carry=0
while(i>0):
    curr_dist=10-(int(num[i])+carry)
    total+=curr_dist
    carry=1
    i-=1

total=total+9
print(total)
