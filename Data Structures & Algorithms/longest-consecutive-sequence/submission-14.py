class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        length = 1
        max_len = 1

        for i in range(1,len(nums)):

            if  nums[i] == nums[i-1]:
                continue

            if nums[i] == nums[i-1]+1:
                length += 1
            else:
                length = 1
            
            max_len = max(max_len,length)

        return max_len

        