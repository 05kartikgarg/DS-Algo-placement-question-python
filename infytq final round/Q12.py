s=input()
even,odd=[],[]
sp_ch=0

for i in s:
    if not(i.isalnum()):
        sp_ch+=1
    if i.isdigit():
        if int(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
if sp_ch%2!=0:
    odd,even=even,odd

for i in range(max(len(even),len(odd))):
    if i<len(even):
        print(even[i],end='')
    if i<len(odd):
        print(odd[i],end='')

'''
Input: A5c67r21i@p#8t
Output: 652781
'''
