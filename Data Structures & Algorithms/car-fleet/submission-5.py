class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        fleets = []
        for i in range(len(position)):
            fleets.append([position[i], speed[i]])

        fleets.sort(reverse=True)
        
        stack = []

        for i in range(len(fleets)):
            t = (target - fleets[i][0]) / fleets[i][1]

            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)
            
            