"""13. Rotate Array to the Left
Given an array of N elements and an integer D, rotate the array to the left by D positions.
A left rotation by one position moves the first element to the end.
Example:
Input: Array = [1, 2, 3, 4, 5], D = 2
After first rotation: [2, 3, 4, 5, 1]
After second rotation: [3, 4, 5, 1, 2]
Output:
[3, 4, 5, 1, 2]
Efficient target:
Time complexity O(N)
Auxiliary space O(1), using the reversal algorithm."""

class Solution:
    def RotateArrayLeft(self,A,D):
        length=len(A)
        if length==0:
            return []
        D=D%length
        return A[D:] + A[:D]

A=[int(x) for x in input().split()]
D=int(input())
obj=Solution()
result=obj.RotateArrayLeft(A,D)
print(result)

