class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1) != len(sentence2):
            return False
        
        # Create a set of pairs for O(1) lookup. 
        # Include both (a, b) and (b, a) since similarity is symmetric.
        adj = set()
        for u, v in similarPairs:
            adj.add((u, v))
            adj.add((v, u))

        for i in range(len(sentence1)):
            w1, w2 = sentence1[i], sentence2[i]
            # Words are similar if they are the same OR if they are in similarPairs
            if w1 != w2 and (w1, w2) not in adj:
                return False
        
        return True