class Solution:
    def runningSum(self, L):
        n=len(L)
        ans=[L[0]]
        for i in range(1,n):
            x=ans[i-1]+L[i]
            ans.append(x)

        return ans
num= [int(x) for x in input("enter nos. seperated by spaces: ").split()]

obj = Solution()
result = obj.runningSum(num)
print("Running Sum:", result)