class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        notEqual = []
        indices_to_remove = []  # Store indices to remove after iterating

        for i, n in enumerate(nums):
            if n != val:
                notEqual.append(n)
            else:
                indices_to_remove.append(i)

        # Remove elements from 'nums' using the indices gathered
        for i in reversed(indices_to_remove):
            nums.pop(i)

        lenNE = len(notEqual)
        return lenNE
