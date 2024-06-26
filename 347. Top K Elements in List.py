class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        countnums= {}
        freq = [[] for i in range(len(nums)+ 1)]


        for n in nums:
            countnums[n] = 1 + countnums.get(n,0)

        for n , c in countnums.items():
            freq[c].append(n)

        
        res = []

        for i in range(len(freq) - 1 , 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
