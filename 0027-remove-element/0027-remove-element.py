class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = now = 0
        while now < len(nums):
            if nums[now] != val:
                nums[k] = nums[now]
                k+=1
            now+=1
        return k
        