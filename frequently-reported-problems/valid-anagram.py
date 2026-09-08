"""Given two strings S1 and S2, determine whether they are anagrams.
Twostrings are anagrams if they contain exactly the same characters with the same frequencies,
but possibly in a different order.
Example:
Input:
S1 =listen
S2 =silent
Output:
Valid Anagram
Example:
Input:
S1 =hello
S2 =world
Output:
Not anAnagram
For lowercase English letters, a frequency array of size 26 can be used."""

class Solution:
    def ValidAnagram(self,S1,S2):
        S1=S1.lower()
        S2=S2.lower()
        dict1={}
        for char in S1:
            if char in dict1:
                dict1[char]=dict1[char]+1
            else:
                dict1[char]=1
        dict2={}
        for char in S2:
            if char in dict2:
                dict2[char]=dict2[char]+1
            else:
                dict2[char]=1
        if dict1 == dict2:
            return "Valid Anagram"
        else:
            return "Not an Anagram"

S1=str(input())
S2=str(input())
obj=Solution()
result=obj.ValidAnagram(S1,S2)
print(result)

