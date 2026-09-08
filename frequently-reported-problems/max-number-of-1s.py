"""15. Maximum Consecutive 1s
Given a binary array containing only 0 and 1, find the maximum number of consecutive 1s.
Example:
Input: [1, 1, 0, 1, 1, 1]
Output: 3
Explanation:
The longest consecutive sequence of 1s is [1, 1, 1], whose length is 3.
Expected complexity:
Time: O(N)
Auxiliary space: O(1)"""

class Solution:
    def MaxCon(self,A):
        current_count=0
        max_count=0
        for num in A:
            if num==1:
                current_count=current_count+1
                if current_count>max_count:
                    max_count=current_count
            else:
                current_count=0
        return max_count

A=[int(x) for x in input().split()]
obj=Solution()
result=obj.MaxCon(A)
print(result)

