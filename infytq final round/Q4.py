import re
s=input()
digits=[i for i in set(s)if i.isdigit()]
digits.sort()
digits.reverse()
num=int(''.join(digits))
if num%2==0:
    print(num)
else:
    n=len(digits)
    for i in range(n-1,0,-1):
        if int(digits[i])%2==0:
            a=digits[i]
            digits.remove(a)
            digits.insert(n-1,a)
            even=int(''.join(digits))
            print(even)
            break
    else:
        print(-1)
