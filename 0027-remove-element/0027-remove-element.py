class Solution(object):
    def removeElement(self, nums, val):
        if not nums and not val:
            return 0
        slow = 0
        for fast in range (0, len(nums)):
            if nums[fast] != val:
                if fast != slow:
                    nums[slow] = nums[fast]
                slow += 1
        return slow