class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_water = 0

        while left < right:
            height = 0

            if heights[left] < heights[right]:
                height = heights[left]
            else:
                height = heights[right]

            min_height = height
            width = right - left

            max_water = max(max_water, height*width)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_water


