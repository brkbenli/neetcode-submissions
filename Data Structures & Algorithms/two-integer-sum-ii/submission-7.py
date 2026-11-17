class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while right > left:
            twoSum = numbers[left] + numbers[right]
            print(numbers[right])
            print(numbers[left], "hi")
            if twoSum > target:
                right -= 1
            elif twoSum < target:
                left += 1
            else:
                result = [left + 1, right + 1]
                break
        return result