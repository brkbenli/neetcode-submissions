class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while right > left:
            if numbers[right] + numbers[left] == target:
                return [numbers[left], numbers[right]]
            if target > numbers[left] + numbers[right]:
                left += 1
            if target < numbers[left] + numbers[right]:
                right -= 1
        