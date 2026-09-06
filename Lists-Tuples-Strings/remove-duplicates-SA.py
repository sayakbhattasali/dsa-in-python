class Solution:
    def removeDuplicates(self,Arr):
        n=len(Arr)
        start=0
        for i in range(1,n):
            if Arr[i] != Arr[start]:
                start = start+1
                Arr[start]=Arr[i]
        return start+1

num=[int(x) for x in input("enter nos. seperated by spaces: ").split()]

obj=Solution()
result=obj.removeDuplicates(num)
print("No. of unique elements: ",result)
print("Unique elements: ", num[:result])