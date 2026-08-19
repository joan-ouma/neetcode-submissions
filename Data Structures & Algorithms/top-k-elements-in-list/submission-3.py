class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the occurrences of each number
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Step 2: Create buckets where the index is the frequency
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
            
        # Step 3: Iterate backwards through the buckets
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # If we have reached k elements, we are done
                if len(res) == k:
                    return res