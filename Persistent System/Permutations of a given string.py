def permute(nums):
    result=[]
    if(len(nums)==1):
        return [nums[:]]

    for i in range(len(nums)):
        n=nums.pop(0)
        perms=permute(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result

s=input()
nums=[i for i in s]
res=permute(nums)
for i in res:
    print(''.join(i),end=' ')