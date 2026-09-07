"""7. Palindrome
Given a string or integer, determine whether it reads the same forward and backward.
For a string, compare characters from both ends moving toward the center. For an integer, the
digits can similarly be reversed and compared with the original number.
Example:
Input: madam
Output: Palindrome
Example:
Input: hello
Output: Not a Palindrome."""

class Solution:
    def Palindrome(self,N):
        length=len(N)
        left=0
        right=length-1
        while left<right:
            if N[left] != N[right]:
                return ("Not a palindrome")
            left=left+1
            right=right-1
        return ("Is a palindrome")


entry=str(input("Enter your number/word: "))
obj=Solution()
result=obj.Palindrome(entry)
print(result)
