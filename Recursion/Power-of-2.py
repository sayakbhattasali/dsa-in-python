def IsPowerOfTwo(n):
    if(n<=0):
        return False
    if(n==1):
        return True
    if(n%2!=0):
        return False
    return IsPowerOfTwo(n//2)
print(IsPowerOfTwo(25))


