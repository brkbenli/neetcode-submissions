class Solution:
    def trap(self, height: List[int]) -> int:
    
        maxL = []
        maxHeightL = 0
        for i in range(len(height)):
            maxL.append(maxHeightL)
            maxHeightL = max(maxHeightL, height[i])

        maxR = []
        maxHeightR = 0
        for i in range(len(height) - 1, -1, -1):
            maxR.append(maxHeightR)
            maxHeightR = max(maxHeightR, height[i])
        maxR.reverse()
        
        currSum = 0
        for i in range(len(height)):
            if min(maxR[i], maxL[i]) - height[i] > 0:
                currSum += min(maxR[i], maxL[i]) - height[i]

        return currSum