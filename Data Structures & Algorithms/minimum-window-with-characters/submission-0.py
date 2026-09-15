class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        s_map = defaultdict(int) #keep track of current window
        t_map = defaultdict(int) #freq of what we need in the window
        left, right = 0,0
        bestL, bestR = 0,0
        shortest = float('inf')

        #frequency map of t 
        for char in t:
            t_map[char] += 1

         #while right is in range, increment it until the chars in t are in the substring, then move left until it is not a valid substring. at that point record the length and compare against the shortest length. at the end return shortest length. 

        #for each character in s
        for right in range(len(s)):        
            s_map[s[right]] += 1
            
            #valid sub if true since s_map holds all req chars
            
            valid = True

            for char, val in t_map.items():
                if s_map[char] < val:
                    valid = False
                
            
            while valid:
                dist = (right - left) + 1
                if dist < shortest:
                    shortest = dist
                    bestL = left
                    bestR = right

                s_map[s[left]] -= 1
                if s_map[s[left]] == 0:                    
                    del s_map[s[left]]    
                left += 1

                #check if new window still valid
                for char, val in t_map.items():
                    if s_map[char] < val:
                        valid = False


        return "" if shortest == float('inf') else s[bestL : bestR + 1]
            


            
            


