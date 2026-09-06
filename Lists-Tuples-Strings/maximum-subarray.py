# Given an integer array, find the sub array with largest sum and return its sum

class Solution:
    def maxSubArray(self, Arr):
        max_sum = Arr[0]
        current_sum = 0
        for x in Arr:
            current_sum = current_sum + x
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum

num = [int(x) for x in input("Enter no. seperated by spaces: ").split()]

obj = Solution()
result = obj.maxSubArray(num)
print("Maximum Subarray Sum: ", result)
