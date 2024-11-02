class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
    
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
                  "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
                  "..-", "...-", ".--", "-..-", "-.--", "--.."]
    

        morse_dictionary = {chr(i + ord('a')): code for i, code in enumerate(morse_code)}
    
        # Set to hold unique transformations
        tran = set()
    
        # Transform each word into its Morse code equivalent
        for word in words:
            trans = ''.join(morse_dictionary[char] for char in word)
            tran.add(trans)
    
        
        return len(tran)