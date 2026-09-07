"""2. Divisible Sum Difference
Given two integers N and M, calculate the difference between:
1. The sum of all integers from 1 to N that are divisible by M.
2. The sum of all integers from 1 to N that are not divisible by M.
Return the absolute difference between the two sums.
Example:
Input: N = 10, M=3
Divisible by 3: 3 + 6 + 9 =18
Not divisible by 3: 1 + 2 +4 + 5+7+8+10=37
Output: 19
Constraints:
•NandMarepositiveintegers.
•1≤M≤N."""

class Solution:
    def DivisibleSumDifference(self,N,M):
        num1=0
        num2=0
        if (1<=M<=N):
            for i in range(1,N+1):
                if i%M==0:
                    num1=num1+i
                else:
                    num2=num2+i
            return abs(num1-num2)
        else:
            return ("Invalid Input")


N=int(input("Enter value of N: "))
M=int(input("Enter value of M: "))
obj=Solution()
result=obj.DivisibleSumDifference(N,M)
if result == "Invalid Input":
    print(result)
else:
    print("The Output Is: ", result)
