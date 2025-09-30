class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        1. 브루트포스(전체 탐색) 접근(가장 단순한 방법)
        - 배열의 모든 쌍을 확인해서 합이 target인지 확인하는 방법 
        - 시간 복잡도: O(n^2)
        - 공간 복잡도: O(1)
        2. 해시맵 사용(효율적인 방법)
        - 각 숫자를 확인하면서, target - nums[i]가 이미 나온 적이 있는지 확인
        - 이미 나왔다면, 두 숫자의 합이 target
        - 시간/공간 복잡도: O(n)

        """
        num_to_idx = {} # {num: idx}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_idx:
                return [num_to_idx[complement], i]
            num_to_idx[num] = i
            