
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


if __name__ == "__main__":
    solver = Solution()

    # Example 1:
    # nums = [2,7,11,15], target = 9
    # Output: [0,1]
    print(solver.twoSum([2, 7, 11, 15], 9))  # [0, 1]

    # Example 2:
    # nums = [3,2,4], target = 6
    # Output: [1,2]
    print(solver.twoSum([3, 2, 4], 6))  # [1, 2]

    # Example 3:
    # nums = [3,3], target = 6
    # Output: [0,1]
    print(solver.twoSum([3, 3], 6))  # [0, 1]
