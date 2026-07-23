class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # Solution 1: 정렬 후 연속된 숫자를 세는 것 O(n log n) 
        # if not nums:
        #     return 0
        # nums.sort()
        # longest = 1
        # current = 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1] + 1:
        #         current += 1
        #         longest = max(longest, current)
        #     elif nums[i] != nums[i-1]:
        #         current = 1
        # return longest

        # Solution 2: Set(집합) + "시작점 찾기" 트릭
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # 1. 이 숫자가 수열의 "시작점"인지 확인
            if num - 1 not in num_set:
                # 2. 시작점이라면, 연속된 다음 숫자들을 계속 세어나감
                current_num = num
                current_len = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_len += 1
                longest = max(longest, current_len)

        return longest