class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack_idx = []
        res = [0] * len(temperatures)
        for i,t in enumerate(temperatures):
            while stack_idx and t > temperatures[stack_idx[-1]]:
                res[stack_idx[-1]] = i - stack_idx[-1]
                stack_idx.pop()
            stack_idx.append(i)
        return res
                