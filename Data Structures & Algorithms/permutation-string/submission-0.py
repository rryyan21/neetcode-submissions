class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False    
        
        s1map = defaultdict(int)
        s2map = defaultdict(int)

        for i in range(len(s1)):
            s1map[s1[i]] += 1
            s2map[s2[i]] += 1

        if s1map == s2map:
            return True
            
        for right in range(len(s1), len(s2)):
            new_char = s2[right]
            s2map[new_char] += 1

            old_char = s2[right - len(s1)]
            s2map[old_char] -= 1

            if s2map[old_char] == 0:
                del s2map[old_char]

            if s1map == s2map:
                return True

        return False

            
            