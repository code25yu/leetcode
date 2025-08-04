class Solution(object):
    def findLHS(self, nums):
        max_len = 0
        freq = Counter(nums)
        for key in freq:
            if key + 1 in freq:
                now_len = freq[key] + freq[key + 1]
                max_len = max(max_len, now_len)
        return max_len