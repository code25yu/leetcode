class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Solution 1
        # n = len(nums)
        # seen = []
        # for index in range(n):
        #     if nums[index] in seen:
        #         return True
        #     seen.append(nums[index])
        # return False

        # Solution 2
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # Solution 3
        return len(set(nums)) != len(nums)