a=int(input())
b=int(input())

def cbr(a,b):
    a,b=b,a
    print("Inside ",a,b)
    
print("Outside ",a,b)
cbr(a,b)
