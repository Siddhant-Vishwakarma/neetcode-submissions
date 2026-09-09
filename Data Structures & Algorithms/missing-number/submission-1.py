class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        org_sum = n*(n+1)//2
        curr_sum = 0

        for i in nums:
            curr_sum += i
        
        missing_num = org_sum - curr_sum

        return missing_num
        