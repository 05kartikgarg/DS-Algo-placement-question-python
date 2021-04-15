s=input()
result=""
for i in range(1,len(s),2):
    result+=str(int(s[i])**2)
print(result[0:4])
