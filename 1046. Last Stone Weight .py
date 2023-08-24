import heapq


class Solution:
    def lastStoneWeight(self, stone: list[int]) -> int:
        stones = [-s for s in stones]  # putting into a lsit and multiple by -1
        heapq.heapify(stones)  # linear time operations
        # * want to continue this while the numbers of stone sis greater than 1 can stop at 1 or 0 stones
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:

                # how to add to the heap heappush
                heapq.heappush(stones, first - second)
        stones.append(0)  # add zero if there is no numbers in list
        return abs(stones[0])
