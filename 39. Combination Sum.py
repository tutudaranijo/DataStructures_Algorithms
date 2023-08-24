class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # * back tracking
        res = []

        def dfs(i, cur, total):
            # if we succed
            if total == target:
                res.append(cur.copy())
                return
            # cant find
            if i >= len(candidates) or total > target:
                return

            # first decision where we can include the candidate
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            # second decisions cant use a certain candidate
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res
