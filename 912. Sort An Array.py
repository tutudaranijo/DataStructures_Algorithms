class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def mergesort(arr, l, r):
            if l < r:
                m = (l + r) // 2  # middle
                mergesort(arr, l, m)  # left half
                mergesort(arr, m + 1, r)  # right half
                merge(arr, l, m, r)

        mergesort(nums, 0, len(nums) - 1)
        return nums
