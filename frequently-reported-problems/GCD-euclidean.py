"""5. GCD Using Euclidean Algorithm
Given two positive integers A and B, find their Greatest Common Divisor (GCD).
The GCD is the largest positive integer that divides both A and B without leaving a remainder.
Use the Euclidean algorithm:
GCD(A, B) = GCD(B,A%B)
until B becomes 0.
Example:
Input: A = 48, B= 18
Output: 6
Explanation:
48 %18=12
18 %12=6
12 %6=0
Therefore GCD = 6."""

class Solution:
    def gcd(self,A,B):
        if A<=0 or B<=0:
            return("Invalid Input")
        while (B!=0):
            remainder=A%B
            A=B
            B=remainder
        return A

A=int(input("Enter A: "))
B=int(input("Enter B: "))
obj=Solution()
result=obj.gcd(A,B)
print(result)