class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        
        if len(nums) <= k:
            for i in range(len(nums)):
                res.append(nums[i])
            return res
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                    freq[nums[i]] = count
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            res.append(sorted_freq[i][0])
        return res


