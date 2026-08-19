class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26 #because a - z is 26 letters

            for char in string:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(string)
        
        return list(res.values())

            
        
