class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while r > l:
            length = r - l
            height = min(heights[l], heights[r])
            maxArea = max(maxArea, length * height)
            if heights[r - 1] > heights[l + 1]:
                r -= 1
            else:
                l += 1
        return maxArea