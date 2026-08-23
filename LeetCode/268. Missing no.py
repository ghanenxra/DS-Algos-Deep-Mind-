class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        range_sum = 0
        curr_sum = 0
        curr_sum = sum(nums)
        for i in range(0,n+1):
            range_sum += i
        real_ans = range_sum - curr_sum
        
        return real_ans

        