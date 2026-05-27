class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        sorted_res = sorted(res, key = res.get, reverse=True)

        return sorted_res[:k]