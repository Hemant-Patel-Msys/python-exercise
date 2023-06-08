def indices_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return(i,j)

nums = [ 7,8,2,3,6,9,2,8]
target = 14
print(indices_sum(nums,target))

import  itertools
l = [ 7,8,2,3,6,9,2,8]
target = 14
for numbers in itertools.combinations(l,2):
    if sum(numbers) == target:
        print([l.index(number) for number in numbers])