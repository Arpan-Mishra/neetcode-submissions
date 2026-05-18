class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for wordnum in range(len(words)):
            for charnum in range(len(words[wordnum])):

                #1. row word (character num) is greater that column word
                # 2. column word (word num) is greater than row word
                # if the character at i,j not equal to character at j,i
                if charnum >= len(words) or wordnum >=len(words[charnum])  or words[wordnum][charnum]!=words[charnum][wordnum]:
                    return False
        
        return True
                
