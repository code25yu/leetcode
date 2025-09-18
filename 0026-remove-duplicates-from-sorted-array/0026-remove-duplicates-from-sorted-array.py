class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
#         # 1. while
#         k, now = 0, 1
#         while now < len(nums):
#             if nums[k] != nums[now]:
#                 nums[k + 1] = nums[now]
#                 k+=1
#             now+=1
#         return k + 1   
        
        
        # 2. for
        k = 0
        for now in range(1, len(nums)):
            if nums[now] != nums[k]:
                nums[k+1] = nums[now]
                k+=1
            now+=1
        return k + 1
    
        
