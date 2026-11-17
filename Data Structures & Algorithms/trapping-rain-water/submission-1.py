class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft = []
        maxVal = 0
        for i in range(len(height)):
            maxVal = max(height[i], maxVal)
            maxLeft.append(maxVal)
        maxRight = []
        maxVal = 0
        for i in range(len(height) - 1, -1, -1):
            maxVal = max(height[i], maxVal)
            maxRight.append(maxVal)
        maxRight.reverse()

        minList = []
        for i in range(len(height)):
            minList.append(min(maxLeft[i], maxRight[i]))

        print(maxLeft)
        print(maxRight)
        print(minList)
        print(height)

        currSum = 0
        for i in range(len(height)):
            addit = minList[i] - height[i]
            if addit < 0:
                continue
            else:
                currSum += addit
        return currSum