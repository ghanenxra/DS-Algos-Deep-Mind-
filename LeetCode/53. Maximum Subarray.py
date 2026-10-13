class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = current_max = nums[0]
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            max_so_far = max(max_so_far, current_max)
        return max_so_far


#or

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        for i in range(1, len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
        return max(dp)
