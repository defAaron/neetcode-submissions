class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))

            if sorted_word in groups:
                groups[sorted_word].append(strs[i])

            else:
                groups[sorted_word] = [strs[i]]

        return list(groups.values())

        
# start with first word: alphabetically sort letters in word
    # sorted version = key, list that contains the original word = value
# repeat this for rest of words
# store each key-value in dictionary groups, each word in an list assigned to its alphabetically sorted version
# when storing a word, first check if alphabetically sorted word already exists in groups: if it does: add new word to the value of its corresponding key
#return groups