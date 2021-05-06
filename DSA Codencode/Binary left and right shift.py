# << - left shift operator
# >> - right shift operator
# n=n<<i - left shifting n , i times then the resulting number would be equal to
# n=n*(2^i)
def leftshift(n,i):
    r=n<<i # left shifting n , i times
    print(n,"<<",i,"=",r)
leftshift(5,4)

#------------------------------------------------------------------------

# n=n>>i - right shifting n , i times then the resulting number would be equal to
# n=n/(2^i)
def rightshift(n,i):
    r=n>>i # right shifting n , i times
    print(n,">>",i,"=",r)
rightshift(8,2)
rightshift(100,5)
