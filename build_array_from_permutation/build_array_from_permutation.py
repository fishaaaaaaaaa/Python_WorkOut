def buildArray(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans


print(buildArray([0,2,1,5,3,4]))
print(buildArray([5,0,1,2,3,4]))
