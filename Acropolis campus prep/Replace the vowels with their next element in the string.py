s=input()
temp=[i for i in s]
d={'a':'b','e':'f','i':'j','o':'p','u':'v'}

for i in range(len(temp)):
    if temp[i] in ['a','e','i','o','u']:
        temp[i]=d[temp[i]]
print("".join(temp))
