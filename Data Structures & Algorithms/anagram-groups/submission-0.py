class Solution:
    def isAnagram(self, str1: str, str2: str):
        if (len(str1) != len(str2)):
            return False

        counts_1 = [0 for _ in range(0, 26)]
        counts_2 = [0 for _ in range(0, 26)]

        for i in range (0, len(str1)):
            counts_1[ord(str1[i]) - ord('a')] += 1
            counts_2[ord(str2[i]) - ord('a')] += 1

        for i in range(0, 26):
            if counts_1[i] != counts_2[i]:
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        for s in strs:
            for arr in res:
                if self.isAnagram(arr[0], s):
                    arr.append(s)
                    break
            else:
                res.append([s])
        
        if len(res) == 0:
            res.append([""])
        return res