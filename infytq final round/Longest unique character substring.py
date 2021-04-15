#longest unique character substring

s=input()
l=len(s)
uniq=''
for i in range(l):
    substr=s[i]
    for j in range(i+1,l):
        substr+=s[j]
        sub_len=len(substr)
        if sub_len>=3 and len(set(substr))==sub_len:
            if len(uniq)<sub_len:
                uniq=substr
if len(uniq)==0:
    print("-1")
else:
    print(uniq)
