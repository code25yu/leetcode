class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        k = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                k+=1
        return k