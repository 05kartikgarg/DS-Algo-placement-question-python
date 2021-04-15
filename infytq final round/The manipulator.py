def calculator(string):
    length=len(string)
    s=list(string)
    for i in range(length):
        if s[i]=='#':
            for j in range(i-1,-1,-1):
                if s[j].isalpha():
                    if s[j]=='Z':
                        s[j]='A'
                        break
                    else:
                        s[j]=chr(ord(s[j])+1)
                        break
    return (''.join(s))

for _ in range(int(input())):
    str1=input()
    str2=input()
    s1=calculator(str1)
    s2=calculator(str2)
    sa=''.join(s1.split('#'))
    sb=''.join(s2.split('#'))
    if sa==sb:
        print("Yes")
    else:
        print("No")