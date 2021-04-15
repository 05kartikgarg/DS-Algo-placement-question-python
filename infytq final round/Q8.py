s=input()
l=len(s)
mid=l//2
for i in range(mid,0,-1):
    prefix=s[0:i]
    suffix=s[l-i:l]

    if prefix==suffix:
        print(len(prefix))
        break
