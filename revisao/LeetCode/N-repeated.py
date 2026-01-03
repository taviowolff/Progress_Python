from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1

# Example usage:
sol = Solution()  
result = sol.repeatedNTimes([1, 2, 2, 3])
print(result)