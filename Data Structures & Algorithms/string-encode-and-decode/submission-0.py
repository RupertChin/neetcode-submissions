class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '-'
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        if len(s) == 0:
            return res
        
        i = 0
        while (i < len(s)):
            delim = s.find('-', i)
            str_len = int(s[i:delim])
            res.append(s[delim+1:delim+str_len+1])
            i = delim + str_len + 1
        
        return res
