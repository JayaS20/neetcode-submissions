class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            res=1
            for j in range(len(nums)):
                if j != i:
                    res *= nums[j]
                else:
                    pass
            output.append(res)
        return output
