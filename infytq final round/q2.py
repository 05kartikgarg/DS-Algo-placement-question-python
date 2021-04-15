'''
#Method 1

s=input()
out=""
for i in s:
    if i not in out:
        out+=i
print(out[-1::-1])

'''

#Method 2

s=input()
d=list(dict.fromkeys(s))
d.reverse()
print("".join(d))
