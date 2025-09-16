class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_nums = 0
        now = 0
        for n in nums:
            if n == 1:
                now += 1
                max_nums = max(max_nums, now)
            else:
                now = 0
        return max_nums
