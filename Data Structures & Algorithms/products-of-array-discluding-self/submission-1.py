class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        prod = 1
        for i in range(len(nums)):
            prefix.append(prod * nums[i])
            prod *= nums[i]
        prod = 1
        postfix = []
        for i in range(len(nums) - 1, -1, -1):
            postfix.append(nums[i] * prod)
            prod *= nums[i]
        postfix.reverse()

        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(postfix[i + 1])
            elif i == len(nums) - 1:
                output.append(prefix[i - 1])
            else:
                output.append(prefix[i - 1] * postfix[i + 1])
        return output


        
