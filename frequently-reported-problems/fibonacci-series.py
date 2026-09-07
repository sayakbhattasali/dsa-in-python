"""6. Fibonacci Series
Given an integer N, print the first N terms of the Fibonacci series.
The Fibonacci sequence starts with 0 and 1. Each subsequent term is the sum of the previous
two terms.
Example:
Input: N = 7
Output: 0 1 1 2 3 5 8
Constraints:
• N≥1
The iterative solution should be preferred when only the sequence is required, as it uses O(N)
time and O(1) auxiliary space"""

class Solution:
    def FibonacciSeries(self,N):
        if N<=0:
            return("Invalid input")
        elif N==1:
            return ([0])
        else:
            fib_series=[0,1]
            a=0
            b=1
            for i in range(2,N):
                c=a+b
                fib_series.append(c)
                a=b
                b=c
            return fib_series

num=int(input("No. of elements: "))
obj=Solution()
result=obj.FibonacciSeries(num)
print(result)



        