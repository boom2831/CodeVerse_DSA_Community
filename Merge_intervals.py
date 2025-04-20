from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort intervals based on the starting time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:  # Overlapping intervals
                last[1] = max(last[1], current[1])  # Merge
            else:
                merged.append(current)  # No overlap

        return merged
sol = Solution()

print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]
print(sol.merge([[1, 4], [4, 5]]))                    # Output: [[1, 5]]
print(sol.merge([[1, 10], [2, 3], [4, 5]]))           # Output: [[1, 10]]
