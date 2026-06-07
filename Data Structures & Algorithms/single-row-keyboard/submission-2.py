class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        cur_i = 0

        t = 0
        word_map = {}
        for i in range(len(keyboard)):
            word_map[keyboard[i]] = i

        for c in word:
            tc = abs(cur_i - word_map[c]) 
            t+=tc
            cur_i = word_map[c]
        
        return t



