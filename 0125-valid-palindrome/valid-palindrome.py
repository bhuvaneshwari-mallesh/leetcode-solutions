class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        left = 0
        right = len(cleaned) - 1

        while(left < right):
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
