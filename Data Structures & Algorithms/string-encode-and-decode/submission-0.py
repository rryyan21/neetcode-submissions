class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            leng = len(s)
            res.append(str(leng) + '#')
            
            for c in s:
                res.append(c)
        return ''.join(res)
            
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            leng = int(s[i:j])
            word = s[j + 1 : j + 1 + leng]
            res.append(word)
            i = j + 1 + leng

        return res
