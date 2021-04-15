s=input()
num1=0
num2=""
ind1=s.index("4")
ind2=s.index("7")
for i in range(len(s)):
    if (i<ind1 or i>ind2)and s[i]!=",":
        num1+=int(s[i])
    if (i>=ind1 and i<=ind2) and s[i]!=",":
        num2+=s[i]
result=num1+int(num2)
print(result)
