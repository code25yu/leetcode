class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution1
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer

        # # Solution2
        # # O(n) 추가 공간 버전 (비교용)
        # def productExceptSelf(self, nums):
        #     n = len(nums)
        #     left = [1] * n   # 왼쪽 누적곱 배열 (추가 공간!)
        #     right = [1] * n  # 오른쪽 누적곱 배열 (추가 공간!)
        #     answer = [1] * n
            
        #     for i in range(1, n):
        #         left[i] = left[i-1] * nums[i-1]
            
        #     for i in range(n-2, -1, -1):
        #         right[i] = right[i+1] * nums[i+1]
            
        #     for i in range(n):
        #         answer[i] = left[i] * right[i]
            
        #     return answer