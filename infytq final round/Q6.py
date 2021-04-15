s=input()
s_final=''
a=s.split(',')
for i in a:
    x,y=i.split(':')
    length=len(x)
    maximum=0
    for j in y:
        if int(j)<=length and int(j)>=int(maximum):
            maximum=j
    if maximum==0:
        s_final+='X'
    else:
        s_final+=x[int(maximum)-1]
print(s_final)


'''
Input: Anchal:23581,Aman:57568,Sonakshi:34848,Ria:14585
Output: aXiR
'''
