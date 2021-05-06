'''
#print(1-N)

n=int(input())

def print1n(n):
    if n==1:
        print(n)
        return
    print1n(n-1)
    print(n)

print1n(n)

#print N-1

n=int(input())

def print1n(n):
    if n==1:
        print(n)
        return
    print(n)
    print1n(n-1)

print1n(n)

'''
#Factorial

n=int(input())
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(n))