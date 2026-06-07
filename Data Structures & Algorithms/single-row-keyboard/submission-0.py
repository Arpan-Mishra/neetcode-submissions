class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        cur_i = 0

        t = 0

        word_map = {w:i for (i,w) in enumerate(keyboard)}

        for c in word:
            tc = abs(cur_i - word_map[c]) 
            t+=tc
            cur_i = word_map[c]
        
        return t
        


