"""4. Happy Number
Given a positive integer N, determine whether it is a Happy Number.
Repeatedly replace the number by the sum of the squares of its digits. If the process eventually
reaches 1, the number is happy. If it enters a cycle that never reaches 1, it is not happy.
Example 1:
Input: 19
Process:
19  -> 1^2 + 9^2 = 82
82  -> 8^2 + 2^2 = 68
68  -> 6^2 + 8^2 = 100
100 -> 1^2 + 0^2 + 0^2 = 1
Output: Happy Number
Example 2:
Input: 2
Output: Not a Happy Number"""

class Solution:
    def HappyNumber(self,N):
        if N<=0:
            return ("Invalid Input")
        else:
            seen=set()
            while N != 1 and N not in seen:
                seen.add(N)
                total=0
                while N>0:
                    digit=N%10
                    total=total+(digit**2)
                    N=N//10
                N=total
            if N == 1:
                return ("Happy Number")
            else:
                return ("Not Happy Number")

N=int(input("Enter the number: "))
obj=Solution()
Result=obj.HappyNumber(N)
print(Result)

