p=int(input())
t=int(input())
bank=[]

for k in range(2):
    n=int(input())
    sum1=0

    for i in range(n):
        yrs,mir=map(float,input().split())
        yrs=int(yrs)
        sq=(1+mir)**(yrs*12)
        emi=(p*(mir))/(1-1/sq)
        sum1+=emi
    bank.append(sum1)

if(bank[0]<bank[1]):
    print("Bank A",end='')
else:
    print("Bank B",end='')
