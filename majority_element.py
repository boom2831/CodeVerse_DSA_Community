from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
sol = Solution()

print(sol.majorityElement([3, 2, 3]))             # Output: 3
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
