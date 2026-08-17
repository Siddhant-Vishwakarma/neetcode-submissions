class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        for key,val in freq.items():
            if val > 1:
                return True
                break
        return False