class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = set()
        for index in range(len(nums)):
            if nums[index] in seen:
                return True
            seen.add(nums[index])
            if len(seen) > k:
                seen.remove(nums[index - k])
        return False