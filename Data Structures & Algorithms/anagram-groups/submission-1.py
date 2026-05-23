from collections import defaultdict

class Solution:
    # def isAnagram(self, str1: str, str2: str): 
    #     if (len(str1) != len(str2)):
    #         return False

    #     counts_1 = [0] * 26
    #     counts_2 = [0] * 26

    #     for i in range (0, len(str1)):
    #         counts_1[ord(str1[i]) - ord('a')] += 1
    #         counts_2[ord(str2[i]) - ord('a')] += 1

    #     for i in range(0, 26):
    #         if counts_1[i] != counts_2[i]:
    #             return False
    #     return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            groups[tuple(key)].append(s)

        return list(groups.values())