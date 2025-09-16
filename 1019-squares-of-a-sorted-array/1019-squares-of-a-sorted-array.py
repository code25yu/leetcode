class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

#         length = len(nums);
#         for i in range(length):
#             nums[i] = nums[i]*nums[i]
#         for j in range(length - 1):
#             for i in range(length - 1 - j):
#                 if nums[i] > nums[i+1]:
#                     tmp = nums[i]
#                     nums[i] = nums[i+1]
#                     nums[i+1] = tmp
#         return nums

        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        pos = n - 1
         
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left] * nums[left]
                left += 1
            else:
                res[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1
        return res
                    