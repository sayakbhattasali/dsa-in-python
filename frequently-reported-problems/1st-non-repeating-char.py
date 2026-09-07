"""8. First Non-Repeating Character
Given a string, find the first character that occurs exactly once in the string.
The character must be returned in the same order in which it appears. If every character repeats,
return an appropriate indication such as-1.
Example:
Input: swiss
Output: w
Explanation:
s appears more than once, w appears once, i appears once, but w is the first non-repeating
character.
Example:
Input: aabb
Output:-1."""

class Solution:
    def NonRepeatingFirst(self,N):
        new={}
        for char in N:
            if char in new:
                new[char]=new[char]+1
            else:
                new[char]=1
        for char in N:
            if new[char] == 1:
                return char
        return -1


N=str(input("Enter a string: "))
obj=Solution()
result=obj.NonRepeatingFirst(N)
print(result)


