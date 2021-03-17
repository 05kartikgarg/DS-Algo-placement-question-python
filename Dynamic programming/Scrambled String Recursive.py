a=input()
b=input()

def solve(a,b):
    if a==b:
        return True
    if len(a)<=1:
        return False
    n=len(a)
    flag=False
    for i in range(1,n):
        if((solve(a[0:i+1],b[n-i:i-1:-1])==True and solve(a[i:n-i+1],b[0:n-i+1])==True) or (solve(a[0:i+1],b[0:i+1])==True and solve(a[i:n-i+1],b[i:n-i+1])==True)):
            flag=True
            break
    return flag
solve(a,b)
'''
a=great
b=eatgr
output: True
'''
'''
# Python3 program to check if a
# given string is a scrambled
# form of another string
def isScramble(S1: str, S2: str):
	
	# Strings of non-equal length
	# cant' be scramble strings
	if len(S1) != len(S2):
		return False

	n = len(S1)

	# Empty strings are scramble strings
	if not n:
		return True

	# Equal strings are scramble strings
	if S1 == S2:
		return True

	# Check for the condition of anagram
	if sorted(S1) != sorted(S2):
		return False

	for i in range(1, n):
		
		# Check if S2[0...i] is a scrambled
		# string of S1[0...i] and if S2[i+1...n]
		# is a scrambled string of S1[i+1...n]
		if (isScramble(S1[:i], S2[:i]) and
			isScramble(S1[i:], S2[i:])):
			return True

		# Check if S2[0...i] is a scrambled
		# string of S1[n-i...n] and S2[i+1...n]
		# is a scramble string of S1[0...n-i-1]
		if (isScramble(S1[-i:], S2[:i]) and
			isScramble(S1[:-i], S2[i:])):
			return True

	# If none of the above
	# conditions are satisfied
	return False

# Driver Code
if __name__ == "__main__":
	
	S1 = "coder"
	S2 = "ocred"
	
	if (isScramble(S1, S2)):
		print("Yes")
	else:
		print("No")

# This code is contributed by sgshah2

'''
