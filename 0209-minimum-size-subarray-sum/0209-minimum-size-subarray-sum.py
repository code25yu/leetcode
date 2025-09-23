class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        now_sum = 0
        min_len = float('inf')
        for r in range(len(nums)):
            now_sum += nums[r]
            while now_sum >= target:
                min_len = min (min_len, r + 1 - l)
                now_sum -= nums[l]
                l += 1
        return 0 if min_len == float('inf') else min_len
