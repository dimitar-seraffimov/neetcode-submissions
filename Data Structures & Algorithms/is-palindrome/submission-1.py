class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # skip non alphanumeric for left pointer
            while left < right and not s[left].isalnum():
                left += 1
            # skip non alphanumeric for right pointer
            while left < right and not s[right].isalnum():
                right -= 1
            # compare thea alphanumeric chars 
            if s[left].lower() != s[right].lower():
                return False
            # move pointers
            left += 1
            right -= 1
        return True