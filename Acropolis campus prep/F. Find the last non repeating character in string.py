MAX = 256
def lastNonRepeating(string, n) :
	freq = [0]*MAX;

	for i in range(n) :
		freq[ord(string[i])] += 1;

	for i in range(n-1,-1,-1) :
		ch = string[i]

		if (freq[ord(ch)] == 1) :
			return ("" + ch)
	
	return "-1"

	
string = "GeeksForGeeks"
n = len(string)
print(lastNonRepeating(string, n))

