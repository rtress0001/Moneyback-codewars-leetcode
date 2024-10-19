class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aieou")
        total_vowels = 0
        
        for i in range(len(word)):
            vowel_set = set()
            for j in range(i,len(word)):
                if word[j] in vowels:
                    vowel_set.add(word[j])
                    if len(vowel_set) == 5:
                        total_vowels+=1
                else:
                    break
        return total_vowels