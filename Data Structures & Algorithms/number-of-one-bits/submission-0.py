class Solution:
    def hammingWeight(self, n: int) -> int:
        binStr = bin(n)
        count = 0
        for i in binStr:
            if i == "1":
                count += 1

        return count