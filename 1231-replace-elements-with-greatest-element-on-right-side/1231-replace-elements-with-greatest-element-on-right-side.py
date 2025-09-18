class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_nums = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = max_nums
            max_nums = max(max_nums, tmp)
        return arr