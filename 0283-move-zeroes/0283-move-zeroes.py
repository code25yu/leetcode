class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        w = r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[w] = nums[r]
                w+=1
            r+=1
        while w < len(nums):
            nums[w] = 0
            w+=1
        return nums
        