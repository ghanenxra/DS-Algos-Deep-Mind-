nums=[3, 1, 4, 2, 0, 8, 6]
n=len(nums)
for i in range(n):
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            temp=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=temp
print(nums)


# In Bubble sort we find maximum element push it to the most right which is its 
# Position it has to gain in sorting then after making it happen we reduce the range
# in new range we dont count that element cuz its already at its right position