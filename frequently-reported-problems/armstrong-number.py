"""3. Armstrong Number
Given a positive integer N, determine whether it is an Armstrong number.
An Armstrong number is a number whose value is equal to the sum of each 
of its digits raised to the power of the total number of digits.
For a three-digit number ABC:
N = A^3 + B^3 + C^3
Example 1:
Input: 153
Output: Armstrong Number
Explanation:
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Example 2:
Input: 123
Output: Not an Armstrong Number"""

class Solution:
    def ArmstrongNumber(self, N):
        if N <= 0:
            return "Invalid Input"
        else:
            num_str=str(N)
            power=len(num_str)
            total=0
            temp=N
            while(temp>0):
                digit=temp%10
                total=total+(digit**power)
                temp=temp//10
            if(total==N):
                return("Armstrong Number")
            else:
                return("Not Armstrong Number")


N=int(input("Enter the number: "))
obj=Solution()
result=obj.ArmstrongNumber(N)
print(result)

        
