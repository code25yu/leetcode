# hash table 
# class Solution(object):
#     def findLHS(self, nums):
#         max_len = 0
#         freq = Counter(nums)
#         for key in freq:
#             if key + 1 in freq:
#                 now_len = freq[key] + freq[key + 1]
#                 max_len = max(max_len, now_len)
#         return max_len

# sort + two pointers / sliding window
class Solution(object):
    def findLHS(self, nums):
        max_len = 0
        start = 0
        nums.sort()
        for end in range(len(nums)):
            while nums[end] - nums[start] > 1:
                start += 1
            if nums[end] - nums[start] == 1:
                max_len = max(max_len, end - start + 1)
        return max_len
                
        