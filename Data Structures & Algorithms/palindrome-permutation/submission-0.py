class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        #all characters have to be in paris except 1

        char_count = Counter(s)
        odd_count = 0

        for t in char_count:
            if char_count[t]%2!=0:
                odd_count+=1
        
        if odd_count>1:
            return False
        else:
            return True

