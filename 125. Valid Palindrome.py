class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1  # l starts on left r starts at right

        while l < r:  # the positions are not =
            # keep moving left pointer to the right till alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # same thing for right but left
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():  # check if the characters is the same
                return False
            l, r = l+1, r-1  # if l != r move it
        return True

    def alphaNum(self, c):
        # ord means unicode
        return (ord('A') <= ord(c) <= ord('Z') or  # checks if its been A-Z
                ord('a') <= ord(c) <= ord('z') or  # check sif between a-z
                ord('0') <= ord(c) <= ord('9'))  # checks if between 0-9
