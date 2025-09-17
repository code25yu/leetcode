class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k, now = 0, 1
        while now < len(nums):
            if nums[k] != nums[now]:
                nums[k + 1] = nums[now]
                k+=1
            now+=1
        return k + 1
