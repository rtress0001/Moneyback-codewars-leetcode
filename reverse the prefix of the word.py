class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        #find the index
        index = word.find(ch)
        #if no ch in word
        if index == -1:
            return word
        #splice the list
        reversed_word = word[:index+1]
        reversed_word = reversed_word[::-1]
        #adding the remaining to the word    
        return reversed_word+word[index+1:]
    
        
    
        
            
                