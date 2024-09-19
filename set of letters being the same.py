class Solution:
    def similarPairs(self, words: List[str]) -> int:
        set_letters = []
        for ele in words:
            set_letters.append(set(ele))
        
        count = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i+1,n):
                if set_letters[i]==set_letters[j]:
                    count += 1
            
        return count
        
        