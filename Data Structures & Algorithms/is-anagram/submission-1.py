class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_letter = s[i]
            s_count[s_letter] = s_count.get(s_letter, 0) + 1

        for j in range (len(t)):
            t_letter = t[j]
            t_count[t_letter] = t_count.get(t_letter, 0) + 1
        
        if s_count == t_count:
            return True
            
        else:
            return False

