class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for wordnum in range(len(words)):
            
            for charnum in range(len(words[wordnum])):

                # false if characters in a word more than number of words (rows > columns) or number of words more than charsv (col>row)
                if charnum >= len(words) or wordnum >= len(words[charnum]) or words[wordnum][charnum] != words[charnum][wordnum]: 
                    return False

                
        return True