class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for i in s:
            if i.isalnum():
                newStr += i.lower()
        reversedStr = newStr[::-1]

        if reversedStr == newStr:
            return True

        else:
            return False