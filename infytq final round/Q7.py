s=input()
s_final=''
a=s.split(',')
for i in a:
    x,y=i.split(':')
    square=0
    for i in y:
        square+=(int(i))**2
    if square%2==0:
        temp=x[-1:-3:-1]
        temp1=temp[::-1]+x[:len(x)-2]
        print(temp1,end=' ')
    else:
        temp=x[0]
        x+=temp
        print(x[1:],end=' ')
print()
        
'''
Input: abcd:1234,bcdgfhf:127836,sdjks:1245
Output: cdab cdgfhfb kssdj
'''
