import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.minHeap, self.k = nums, k
        # ! turning into a heap , its just an array before that
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:  # * if the length is bigger then k then we pop
            heapq.heappop(self.minHeap)
        return self.minHeap[0]  # min value is always at the first  index
