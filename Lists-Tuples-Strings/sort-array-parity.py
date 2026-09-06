#Sort Array By Parity 
class Solution:
    def sortArrayParity(self,Arr):
        n=len(Arr)
        start=0
        for i in range(n):
            if Arr[i]%2==0:
                temp = Arr[i]
                Arr[i]=Arr[start]
                Arr[start]=temp
                start = start+1
        return Arr

num=[int(x)for x in input("Enter no. seperated by spaces: ").split()]

obj=Solution()
result=obj.sortArrayParity(num)
print(result)
