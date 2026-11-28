class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(curr.copy())
                return 
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                curr.append(candidates[i])
                backtrack(i+1, remaining - candidates[i])
                curr.pop()

        backtrack(0, target)

        return res
        