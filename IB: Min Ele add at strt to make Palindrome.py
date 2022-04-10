"""
Approaches:
    
    1. Brute Force: tc: O(N^2) sc: O(1):
        
        a. Loop till string len > 1
        b. Check if the str is a palindrome if yes than break and return res
        c. Else res += 1 and str = str[:-1] ie, remove last ele of str
            Coz the number of elements removed from the last must be added to front to make in a palindrome
    
    2. Using KMP algo LPS array: tc: O(2N) sc: O(N):
        
        a. reverse the str and special char $ than concatenate it on front
        b. Make LPS array with LPS[0] = 0
        c. By subtracting the original strings len - LPS[-1] we will get the ans
    
   Interview Bits: https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic/discussion/p/python-solution-for-problem/73124/1096
   GFG: https://www.geeksforgeeks.org/minimum-characters-added-front-make-string-palindrome/
"""
# Brute Force :-
class Solution:
    
    def solve(self, st):

        res, flag = 0, False
        while len(st) > 1:
            if st == st[::-1]:
                flag = True
                break

            res += 1
            st = st[:-1]

        return res

    
# KMP Algo 

# Returns vector lps for given string str
def computeLPSArray(string):

	M = len(string)
	lps = [None] * M

	length = 0
	lps[0] = 0 # lps[0] is always 0

	# the loop calculates lps[i]
	# for i = 1 to M-1
	i = 1
	while i < M:
	
		if string[i] == string[length]:
		
			length += 1
			lps[i] = length
			i += 1
		
		else: # (str[i] != str[len])
		
			# This is tricky. Consider the example.
			# AAACAAAA and i = 7. The idea is
			# similar to search step.
			if length != 0:
			
				length = lps[length - 1]

				# Also, note that we do not
				# increment i here
			
			else: # if (len == 0)
			
				lps[i] = 0
				i += 1

	return lps

# Method returns minimum character
# to be added at front to make
# string palindrome
def getMinCharToAddedToMakeStringPalin(string):

	revStr = string[::-1]

	# Get concatenation of string,
	# special character and reverse string
	concat = string + "$" + revStr

	# Get LPS array of this
	# concatenated string
	lps = computeLPSArray(concat)

	# By subtracting last entry of lps
	# vector from string length, we
	# will get our result
	return len(string) - lps[-1]

# Driver Code
if __name__ == "__main__":

	string = "AACECAAAA"
	print(getMinCharToAddedToMakeStringPalin(string))
	
    
