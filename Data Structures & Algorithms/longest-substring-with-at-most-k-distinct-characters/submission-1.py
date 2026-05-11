class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        left = right = 0
        char_map = defaultdict(int)
        longest = 0

        while right<len(s):
            
            char_map[s[right]]+=1

            while len(char_map)>k:
                char_map[s[left]]-=1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                
                left+=1
            
            longest = max(longest, right-left+1)

            right+=1
        return longest


