class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        left = 0
        
        count = 0

        if k>len(s):
            return 0

        for right in range(k, len(s)+1):
            
            sub_count = len(set(s[left:right]))
            print(s[left:right])
            print(sub_count)
            if sub_count == k:
                count+=1
            left+=1
            
        return count
            



            


        