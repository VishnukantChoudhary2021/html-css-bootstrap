nums=[10,2,3,55,6,7,9]
n=len(nums)
for i in range(n-1):
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]

print(nums)