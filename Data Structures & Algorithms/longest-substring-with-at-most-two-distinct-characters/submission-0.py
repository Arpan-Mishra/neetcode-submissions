from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        left = 0
        right = 0
        longest_substring = 1

        char_map = defaultdict(int)



        while right<len(s):

            char_map[s[right]]+=1
            
            while len(char_map)>2:
                
                char_map[s[left]]-=1
                if char_map[s[left]]==0:
                    del char_map[s[left]]

                left+=1
            


            longest_substring = max(longest_substring, right-left+1)

            right+=1
        return longest_substring



        