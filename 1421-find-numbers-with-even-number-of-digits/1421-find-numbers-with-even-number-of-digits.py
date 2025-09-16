class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_nums = 0
        for n in nums:
            digit = len(str(n))
            if digit % 2 == 0:
                even_nums += 1
        return even_nums