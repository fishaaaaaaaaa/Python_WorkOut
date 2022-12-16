def two_sum(nums, target):
    
    for i in range(len(nums)):
        
        if nums[i] + nums[i + 1] == target:
            
            return [i, i + 1]

print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))