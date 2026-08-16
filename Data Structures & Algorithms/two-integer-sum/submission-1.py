class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numTbl = {}

        for i, v in enumerate(nums):
            numTbl[v] = i

        for i, v in enumerate(nums):
            w = target - v
            if w in numTbl and numTbl[w] != i:
                return [i, numTbl[w]]

        return []