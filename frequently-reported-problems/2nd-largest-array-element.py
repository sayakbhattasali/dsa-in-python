""" 1. Second Largest Element in an Array
Given an integer array of N elements, find the second largest distinct element in the array.
The second largest element must be different from the largest element. If the array does not
contain at least two distinct values, return an appropriate indication such as-1.
Example:
Input: N = 6, Array = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation:
The largest element is 35 and the second largest distinct element is 34.
Constraints:
• 2≤N
• Elements are integers.
• Duplicate values may be present """

class Solution:
    def SecondLargest(self,Arr):
        unique_elements= list(set(Arr))
        n=len(unique_elements)
        if n<2:
            return -1
        else:
            sorted_elements=sorted(unique_elements)
            return sorted_elements[-2]

num=[int(x) for x in input("Enter nos. seperated by spaces: ").split()]
obj=Solution()
result=obj.SecondLargest(num)
print("Second Largest Element: ",result)