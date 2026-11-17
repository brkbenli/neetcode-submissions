class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for i in s:
            if i.isalnum():
                newStr += i.lower()
        right = len(newStr) - 1
        left = 0
        while right > left:
            if newStr[right] == newStr[left]:
                right -= 1
                left += 1
            else:
                return False
        return True