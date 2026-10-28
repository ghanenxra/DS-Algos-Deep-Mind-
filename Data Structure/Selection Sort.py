nums=[3, 1, 4, 0, 2, 8, 6]
n=len(nums)
for i in range(n):
    min_j=i+1
    for j in range(i+1, n):
        if nums[i]<nums[min_j]:
            min_j=j
        if nums[i]>nums[min_j]:
            temp=nums[i]
            nums[i]=nums[min_j]
            nums[min_j]=temp
print(nums)

""" The Selection sort works by picking the smallest element and move it to bottom
left which makes it to its right position and then we change the range and excluding 
the front element of the previous range
"""