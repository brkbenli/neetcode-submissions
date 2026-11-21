class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count(n):
            binStr = bin(n)
            counting = 0
            for i in binStr:
                if i == "1":
                    counting += 1
            return counting
        res = []
        for i in range(n + 1):
            res.append(count(i))
        return res