class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        memo = {}
        def recurse(i, currSum):
            if currSum == amount:
                return 1
            if i == len(coins) or currSum > amount:
                return 0

            if (i, currSum) in memo:
                return memo[(i, currSum)]
                
            res = recurse(i, currSum + coins[i]) + recurse(i + 1, currSum)
            memo[(i, currSum)] = res
            return res
        return recurse(0, 0)