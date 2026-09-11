class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        mega_string = ""

        for i in range(len(strs)):
            x = len(strs[i])
            string = str(x) + "#" + strs[i]
            mega_string += string
        return mega_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1

            x = int(s[i:j])

            string = s[j + 1:j + 1 + x]
            strs.append(string)

            i = x + 1 + j

            
        return strs


# ENCODING
# read the number of chars in each string
# put the number + "#" in front of each string
# concatenate all strings
# return string
#=========================
# DECODING
# read number in front of substring (say x). IMPORTANT - number can be more than 1 digit, so read until # appears
# word is from string[2] -> string [2 + x]
# slice that portion and add to list strs
# redefine string as unsliced portion
# repeat until x + 2 is len(string)
# return strs