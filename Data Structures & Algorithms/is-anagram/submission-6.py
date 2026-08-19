class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            elif i in hashmap:
                hashmap[i] += 1

        for i in t:
            if i not in hashmap:
                return False
            hashmap[i] -= 1
            
        for i in hashmap:
            if hashmap[i] != 0:
                return False
        
        return True