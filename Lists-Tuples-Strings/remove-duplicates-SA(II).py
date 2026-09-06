class Solution:
    def removeDuplicates(self,Arr):
        n=len(Arr)
        if n<=2:
            return n
        else:
            start=1
            for i in range(2,n):
                if Arr[i] != Arr[start-1]:
                    start = start+1
                    Arr[start]=Arr[i]
            return start+1

num=[int(x) for x in input("enter nos. seperated by spaces: ").split()]

obj=Solution()
result=obj.removeDuplicates(num)
print("No. of unique (II) elements: ",result)
print("Unique elements: ", num[:result])