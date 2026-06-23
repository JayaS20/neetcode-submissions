class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        res = []
        while i<=j:
            if numbers[i] + numbers[j] == target :
                res.append(i+1)
                res.append(j+1)
                break
            elif i < j:
                j -= 1
            elif i == j:
                i = j + 1
                j = len(numbers) - 1
        res.sort()
        return res