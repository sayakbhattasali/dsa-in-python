"""12. Move Zeros to the End
Given an integer array, move all zero elements to the end of the array while maintaining the
relative order of all non-zero elements.
The operation should be performed in-place when possible.
Example:
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
The relative order of 1, 3, and 12 must remain unchanged."""

class Solution:
    def ZerosToEnd(self,A):
        length=len(A)
        p=0
        for i in range(0,length):
            if A[i]!=0:
                temp=A[p]
                A[p]=A[i]
                A[i]=temp
                p=p+1
        return A

A=[int(x) for x in input().split()]
obj=Solution()
result=obj.ZerosToEnd(A)
print(result)


