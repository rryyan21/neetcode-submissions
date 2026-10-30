class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only lowercase alphanumeric characters
        cleaned = "".join([c.lower() for c in s if c.isalnum()])
        # Check if it equals its reverse
        return cleaned == cleaned[::-1]