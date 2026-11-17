class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while r > l:
            length = r - l
            height = min(heights[l], heights[r])
            maxArea = max(maxArea, length * height)
            print(l, r)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea