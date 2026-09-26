class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_t = defaultdict(int)
        hashmap_s = defaultdict(int)

        for char in s:
            hashmap_s[char] += 1

        for char in t:
            hashmap_s[char] -= 1

        for i in hashmap_s.values():
            if i != 0:
                return False


        return True
