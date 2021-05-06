for i in range(int(input())):
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    a = [i+1 for i in range(n)]
    for i in l:
        a.remove(i)
    y,chef,ass=1,[],[]    
    for i in a:
        if y%2!=0:
            chef.append(str(i))
        else:
            ass.append(str(i))
        y+=1    
    print(" ".join((chef)))
    print(" ".join((ass)))
        
    

