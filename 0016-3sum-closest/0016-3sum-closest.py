class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if abs(target - current) < abs(target - result):
                    result = current
                if current == target:
                    return result
                elif current < target:
                    left += 1
                else:
                    right -= 1
        return result