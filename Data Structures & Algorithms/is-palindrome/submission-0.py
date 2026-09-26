class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_s = "".join(char for char in s if char.isalnum())
        final_s = alphanumeric_s.lower()
        if len(final_s) <= 1:
            return True
        a = 0
        b = len(final_s) - 1

        while a < b:
            if final_s[a] == final_s[b]:
                a += 1
                b -= 1

            else:
                return False
        return True

# remove capital letters, non-alphanumeric characters (including spaces)

# a is 0, b is i
# if s[a] = s[b], a += 1, b -= 1
# repeat until a >= b