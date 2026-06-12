class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ls = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j!=i and nums[j] == target - nums[i]:
                    return[i,j]
