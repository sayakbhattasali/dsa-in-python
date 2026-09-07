"""10. Rebound Height
An object dropped from initial height H rebounds to a fixed percentage P after each bounce.
Given H, percentage P, and number of rebounds N, determine the height reached after N rebounds.
Formula: Final Height = H * (P / 100)^N

Example 1:
Input: H = 100, P = 50, N = 2
Output: 25.0

Example 2:
Input: H = 200, P = 20, N = 3
Output: 1.6"""

class Solution:
    def ReboundHeight(self,H,P,N):
        final_height= H* ((P/100)**N)
        return final_height

H=float(input())
P=float(input())
N=int(input())
obj=Solution()
result=obj.ReboundHeight(H,P,N)
print(round(result,2))
