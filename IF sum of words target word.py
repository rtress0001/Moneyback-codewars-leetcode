class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        frist_num = ""
        second_num = ""
        target_num = ""
        
        for ele in firstWord:
            frist_num += str(ord(ele) - ord("a"))
        frist_num = int(frist_num)
        
        for ele in secondWord:
            second_num += str(ord(ele) - ord("a"))
        second_num = int(second_num)
        
        for ele in targetWord:
            target_num += str(ord(ele) - ord("a"))
        target_num = int(target_num)
        
        return frist_num+second_num == target_num