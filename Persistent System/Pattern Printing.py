'''
* 
* * 
* * * 
* * * * 
* * * * *
'''
for i in range(5):
    for j in range(i+1):
        print("*",end=' ')
    print()

print()

#-------------------------------------------------------------------------------

'''
* 
* * * 
* * * * * 
* * * * * * *
'''
k=1
for i in range(1,5):
    for j in range(1,k+1):
        print("*",end=' ')
    k+=2
    print()

print()
#-------------------------------------------------------------------------------
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
num=5
for i in range(num):
    for j in range(num-i-1):
        print(end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

print()

#-------------------------------------------------------------------------------
'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''
num=5
for i in range(num,0,-1):
    for j in range(num-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

print()

#-------------------------------------------------------------------------------
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''
num=5
for i in range(num):
    for j in range(num-i-1):
        print(end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(num-1,0,-1):
    for j in range(num-i):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
    
print()

#-------------------------------------------------------------------------------
'''
* * * * * 
* * * * 
* * * 
* * 
*
'''
num=5
for i in range(num,0,-1):
    for j in range(i):
        print("*",end=' ')
    print()

print()

#-------------------------------------------------------------------------------
'''
 *** 
*   *
*   *
*****
*   *
*   *
*   *
'''
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()

print()
#-------------------------------------------------------------------------------
'''
*****
*    
*    
*****
*    
*    
*****
'''
for row in range(7):
    for col in range(5):
        if (col==0 or (row==0 or row==3 or row==6)):
            print("*",end="")
        else:
            print(end=" ")
    print()

print()       

#-------------------------------------------------------------------------------
'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
'''
n=5
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
print()

#-------------------------------------------------------------------------------
'''
p 
p y 
p y t 
p y t h 
p y t h o 
p y t h o n
'''
inp="python"
n=len(inp)
for i in range(n):
    for j in range(i+1):
        print(inp[j],end=" ")
    print()
print()

#-------------------------------------------------------------------------------
'''
   *   
  * *  
 *   * 
*******
'''
for i in range(1,5):
    for j in range(1,8):
        if (i+j==5) or i==4 or (j-i==3):
            print("*",end="")
        else:
            print(end=" ")
    print()

print()

#-------------------------------------------------------------------------------
'''
      1
     212
    32123
   4321234
  543212345
 65432123456
7654321234567
'''
num=7
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(end=" ")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()

print()













    
