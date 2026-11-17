class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        output = 0
        while r > l:
            distance = r - l
            maxheight = min(heights[l], heights[r])
            output = max(output, maxheight * distance)
            if min(heights[l + 1], heights[r]) * (r - l + 1):
                l += 1
            else:
                r -= 1

        return output