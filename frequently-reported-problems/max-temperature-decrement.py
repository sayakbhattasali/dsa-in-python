"""11. Maximum Temperature Decrement
Given an array representing temperatures recorded over consecutive periods, determine the
maximum decrease between relevant consecutive temperature readings, or the maximum
decrement defined by the particular test specification.
Example:
Input: [30, 25, 20, 22, 18]
Decreases include:
30 -> 25 = 5
25 -> 20 = 5
22 -> 18 = 4
Maximum decrement = 5"""

class Solution:
    def MaxTempDecrement(self,L):
        length=len(L)
        if length<2:
            return 0
        max_dec=0
        for i in range(0,length-1):
            diff=L[i]-L[i+1]
            if diff>max_dec:
                max_dec=diff
        return max_dec

N=[int(x) for x in input().split()]
obj=Solution()
result=obj.MaxTempDecrement(N)
print(result)

