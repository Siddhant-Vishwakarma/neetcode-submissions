class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        res = []
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dict:
                return [dict[target-nums[i]],i]

            dict[nums[i]] = i

            


            

