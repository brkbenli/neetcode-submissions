class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefix.append(product)
        postfix = []
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            postfix.append(product)
        postfix.reverse()

        output = []
        print(prefix)
        if nums:
            output.append(postfix[1])
        for i in range(1, len(nums) - 1):
            output.append(prefix[i - 1] * postfix[i + 1])
        output.append(prefix[len(nums) - 2])
            
        return output