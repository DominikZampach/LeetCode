from typing import List
class Solution:
    #O(n*n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            number = nums[i]
            second_number = target - number
            for j in range(len(nums)):
                if nums[j] == second_number and j != i:
                    return[i, j]
        return [0, 0]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))
print(solution.twoSum([3,3], 6))