class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            match = target - x
            if match in seen:
                return[seen[match],i]
            seen[x] = i
                
                

