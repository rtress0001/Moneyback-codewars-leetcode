class Solution:
    def capitalizeTitle(self, title: str) -> str:
        #declare a storage place for a word
        words = title.split()
        
    
        
        #loop though each letter in the setence
        for i in range(len(words)):
            if len(words[i])>2:
                words[i] = words[i].capitalize()
            else:
                words[i] = words[i].lower()
        
        return " ".join(words)
        
                
            