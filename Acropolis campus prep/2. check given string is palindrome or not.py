s=input()
n=len(s)
flag=1
for i in range(n//2+1):
    if s[i]!=s[n-i-1]:
        flag=0
        break

if flag==0:
    print("False")
else:
    print("True")

'''
s=input()
n=len(s)
for i in range(n//2):
    if s[i]!=s[n-i-1]:
        print(False)
        break
else:
    print(True)

'''


'''
if s==("".join(reversed(s))):
    print(True)
else:
    print(False)
'''
